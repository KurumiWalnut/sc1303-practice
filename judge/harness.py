"""SC1303 judge harness.

Runs in the browser (Pyodide, Python 3.12) and in tools/verify.py (normal Python).

Each test runs in a fresh namespace, in this order:
    provided code -> student code -> test data -> test setup -> test expression
The expected value is worked out in a separate namespace from the provided code and
the same test data, so nothing the student's code does can change it.
"""
import io
import json
import linecache
import sys
import time
import traceback

STUDENT_FILE = "solution.py"
PROVIDED_FILE = "provided.py"
TEST_FILE = "test.py"
CALL_FILE = "test_call.py"
SHOWN_FILES = {STUDENT_FILE, PROVIDED_FILE, TEST_FILE, CALL_FILE}
MAX_TEXT = 3000


def _remember_source(filename, source):
    # Lets tracebacks show the line of code that failed.
    linecache.cache[filename] = (len(source), None, source.splitlines(True), filename)


def _clip(text, limit=MAX_TEXT):
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n... ({len(text) - limit} more characters)"


def _safe_repr(value):
    try:
        return _clip(repr(value))
    except Exception as exc:  # e.g. a broken __repr__ in a student class
        return f"<could not display this value: {exc!r}>"


def _format_error(exc):
    frames = [f for f in traceback.extract_tb(exc.__traceback__) if f.filename in SHOWN_FILES]
    stack = "".join(traceback.StackSummary.from_list(frames).format()) if frames else ""
    if len(stack) > 2000:  # deep recursion: keep the innermost calls
        stack = "  ...\n" + stack[-2000:]
    head = "Traceback (most recent call last):\n" if stack else ""
    tail = "".join(traceback.format_exception_only(type(exc), exc))
    return head + stack + tail


def _no_input(*_args):
    raise EOFError("input() isn't available here. Write the function and return the answer.")


def check_syntax(code):
    """Return a compile error message, or None if the code compiles."""
    _remember_source(STUDENT_FILE, code)
    try:
        compile(code, STUDENT_FILE, "exec")
    except SyntaxError as exc:  # also covers IndentationError
        return "".join(traceback.format_exception_only(type(exc), exc))
    return None


def _expected_value(test, provided):
    ns = {"__name__": "expected"}
    if provided:  # helpers such as build_list may be used by the test data
        exec(compile(provided, PROVIDED_FILE, "exec"), ns)
    if test.get("data"):
        exec(compile(test["data"], "data.py", "exec"), ns)
    return eval(test["expected"], ns)


def _matches(checker, actual, expected):
    if not checker:
        return actual == expected
    ns = {}
    exec(compile(checker, "checker.py", "exec"), ns)
    return bool(ns["check"](actual, expected))


def run_one(code, provided, checker, test_json, limit_ms=3000):
    """Run one test case and return a JSON string describing the outcome."""
    test = json.loads(test_json)
    result = {"status": "internal", "actual": None, "expected": None,
              "stdout": "", "error": None, "ms": 0}

    try:
        expected = _expected_value(test, provided)
    except Exception as exc:
        result["error"] = f"This test case is broken ({exc!r}). Please report it."
        return json.dumps(result)
    result["expected"] = _safe_repr(expected)

    data = test.get("data") or ""
    setup = test.get("setup") or ""
    _remember_source(STUDENT_FILE, code)
    _remember_source(PROVIDED_FILE, provided or "")
    _remember_source(TEST_FILE, setup)
    _remember_source(CALL_FILE, test["expr"])

    ns = {"__name__": "solution", "input": _no_input}
    captured = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = captured
    error = None
    actual = None
    data_seconds = 0.0
    start = time.perf_counter()
    try:
        if provided:
            exec(compile(provided, PROVIDED_FILE, "exec"), ns)
        exec(compile(code, STUDENT_FILE, "exec"), ns)
        if data:  # building the input doesn't count towards the time limit
            data_start = time.perf_counter()
            exec(compile(data, "data.py", "exec"), ns)
            data_seconds = time.perf_counter() - data_start
        if setup:
            exec(compile(setup, TEST_FILE, "exec"), ns)
        actual = eval(compile(test["expr"], CALL_FILE, "eval"), ns)
    except BaseException as exc:  # student code may raise anything, even SystemExit
        error = exc
    finally:
        sys.stdout = real_stdout

    elapsed_ms = (time.perf_counter() - start - data_seconds) * 1000
    result["ms"] = round(elapsed_ms)
    result["stdout"] = _clip(captured.getvalue())

    if error is not None:
        result["status"] = "runtime_error"
        result["error"] = _format_error(error)
        return json.dumps(result)

    result["actual"] = _safe_repr(actual)
    try:
        ok = _matches(checker, actual, expected)
    except Exception as exc:
        ok = False
        result["error"] = "Your answer couldn't be checked: " + "".join(
            traceback.format_exception_only(type(exc), exc))

    if elapsed_ms > limit_ms:
        result["status"] = "tle"
        result["error"] = f"Took {elapsed_ms:.0f} ms; the limit is {limit_ms} ms."
    else:
        result["status"] = "passed" if ok else "wrong"
    return json.dumps(result)
