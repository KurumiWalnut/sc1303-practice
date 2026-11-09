"""Check the problem bank before publishing.

For every problem:
  - the reference solution (solution.py) must pass every test
  - the starter code (starter.py) must fail at least one test
It also checks that tree.json and exams.json only point at problems that exist.

Usage:
    python3 tools/verify.py            # check everything
    python3 tools/verify.py heap-impl  # check some problems
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PROBLEMS = CONTENT / "problems"

spec = importlib.util.spec_from_file_location("harness", ROOT / "judge" / "harness.py")
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)


def load_problem(pid):
    folder = PROBLEMS / pid
    meta = json.loads((folder / "problem.json").read_text())
    for name in ("statement.md", "starter.py", "solution.py"):
        if not (folder / name).exists():
            raise FileNotFoundError(f"{pid}: missing {name}")
    if meta.get("hints"):
        hints = [h for h in (folder / "hints.md").read_text().split("\n---\n") if h.strip()]
        if len(hints) != meta["hints"]:
            raise ValueError(f"{pid}: problem.json says {meta['hints']} hints, hints.md has {len(hints)}")
    provided = (folder / "provided.py").read_text() if meta.get("provided") else ""
    return meta, (folder / "starter.py").read_text(), (folder / "solution.py").read_text(), provided


def run_all(meta, code, provided):
    results = []
    for test in meta["tests"]:
        limit = test.get("timeLimitMs") or meta.get("timeLimitMs", 3000)
        out = harness.run_one(code, provided, meta.get("checker") or "", json.dumps(test), limit)
        results.append((test, json.loads(out)))
    return results


def referenced_problem_ids():
    tree = json.loads((CONTENT / "tree.json").read_text())
    exams = json.loads((CONTENT / "exams.json").read_text())
    ids = []
    for part in tree["parts"]:
        for topic in part["topics"]:
            if topic.get("icon") and not (CONTENT / topic["icon"]).exists():
                raise FileNotFoundError(f"{topic['id']}: missing {topic['icon']}")
            for leaf in topic["leaves"]:
                if leaf["status"] != "ready":
                    continue
                if not (CONTENT / leaf["notes"]).exists():
                    raise FileNotFoundError(f"{leaf['id']}: missing {leaf['notes']}")
                base = leaf.get("base") or []
                ids += [b for b in (base if isinstance(base, list) else [base]) if isinstance(b, str)]
                ids += [p for p in leaf["practice"] if isinstance(p, str)]
    for exam in exams["exams"]:
        ids += exam["problems"]
    return ids


def main(selected):
    failures = 0
    referenced = referenced_problem_ids()
    on_disk = sorted(p.name for p in PROBLEMS.iterdir() if p.is_dir())
    for pid in sorted(set(referenced) - set(on_disk)):
        print(f"MISSING  {pid} is referenced but has no folder")
        failures += 1
    for pid in sorted(set(on_disk) - set(referenced)):
        print(f"UNUSED   {pid} isn't referenced from tree.json or exams.json")

    for pid in selected or on_disk:
        meta, starter, solution, provided = load_problem(pid)
        if meta["id"] != pid:
            print(f"FAIL     {pid}: problem.json id is {meta['id']!r}")
            failures += 1
        sol = run_all(meta, solution, provided)
        bad = [(t, r) for t, r in sol if r["status"] != "passed"]
        slowest = max(r["ms"] for _, r in sol)
        if bad:
            failures += 1
            print(f"FAIL     {pid}: reference solution fails {len(bad)} test(s)")
            for t, r in bad:
                print(f"           - {t['name']}: {r['status']}  got={r['actual']} want={r['expected']}")
                if r["error"]:
                    print("             " + r["error"].strip().replace("\n", "\n             "))
        start = run_all(meta, starter, provided)
        if all(r["status"] == "passed" for _, r in start):
            failures += 1
            print(f"FAIL     {pid}: starter code passes every test")
        if not bad:
            visible = sum(1 for t in meta["tests"] if not t.get("hidden"))
            print(f"ok       {pid}: {len(sol)} tests ({visible} visible), slowest {slowest} ms")
    print()
    print("All good." if not failures else f"{failures} problem(s) need fixing.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
