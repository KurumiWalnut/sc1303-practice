// The coding workspace: problem statement on the left, editor and test results on the right.
import { judge, onJudgeState, warmUp } from "./judge.js";
import { store } from "./storage.js";
import { esc, markdown, highlightCode, icon, difficultyChip, leetcodeLink } from "./ui.js";

const VERDICTS = {
  accepted: { text: "Accepted", tone: "ok" },
  wrong_answer: { text: "Wrong answer", tone: "bad" },
  runtime_error: { text: "Runtime error", tone: "bad" },
  tle: { text: "Time limit exceeded", tone: "warn" },
  compile_error: { text: "Syntax error", tone: "bad" },
  internal: { text: "Judge error", tone: "warn" },
  unavailable: { text: "Python couldn't load", tone: "warn" },
};

const STATUS = {
  passed: { text: "Passed", tone: "ok", icon: "check" },
  wrong: { text: "Wrong answer", tone: "bad", icon: "x" },
  runtime_error: { text: "Runtime error", tone: "bad", icon: "x" },
  tle: { text: "Too slow", tone: "warn", icon: "clock" },
  skipped: { text: "Not run", tone: "muted", icon: "dot" },
  internal: { text: "Judge error", tone: "warn", icon: "x" },
};

const KIND_LABEL = { base: "Base implementation", leetcode: "LeetCode-style", exam: "Exam question" };
const isMac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
const MOD = isMac ? "⌘" : "Ctrl";

// Stays on while moving between problems or exam questions, until the user exits.
let fullscreenOn = false;

/**
 * Mount a workspace into `root`.
 * opts.mode: "practice" (shows hints, solution tab) or "exam" (hides them).
 * opts.codeKey: localStorage key for the draft.
 * opts.onResult(outcome, runMode): called after every Run or Submit.
 * opts.lastOutcome: an outcome to show in the results panel on load.
 * Returns a cleanup function.
 */
export function mountWorkspace(root, problem, opts) {
  const exam = opts.mode === "exam";
  const saved = store.get(opts.codeKey);
  const initialCode = typeof saved === "string" ? saved : problem.starter;
  const visibleCount = problem.tests.filter((t) => !t.hidden).length;
  const hiddenCount = problem.tests.length - visibleCount;
  const hints = exam ? [] : problem.hints || [];

  root.innerHTML = `
    <div class="ws">
      <section class="ws-left" aria-label="Problem">
        <div class="ws-tabs" role="tablist">
          <button class="ws-tab is-active" role="tab" data-pane="desc">Description</button>
          ${hints.length ? `<button class="ws-tab" role="tab" data-pane="hints">Hints <span class="tab-count">${hints.length}</span></button>` : ""}
          ${exam ? "" : `<button class="ws-tab" role="tab" data-pane="sol">Solution</button>`}
        </div>
        <div class="ws-pane" data-pane="desc">
          <div class="prob-head">
            <h2>${esc(problem.title)}</h2>
            <div class="chips">
              ${difficultyChip(problem.difficulty)}
              <span class="chip">${KIND_LABEL[problem.kind] || "Problem"}</span>
              ${exam ? "" : leetcodeLink(problem)}
            </div>
            ${!exam && problem.source ? `<p class="source">From: ${esc(problem.source)}</p>` : ""}
          </div>
          <div class="prose">${markdown(problem.statement)}</div>
          ${problem.prelude ? `
            <details class="provided">
              <summary>${icon("code", 14)} Provided code (already loaded for you)</summary>
              <pre><code class="language-python">${esc(problem.prelude)}</code></pre>
            </details>` : ""}
          <p class="test-note">${visibleCount} sample test${visibleCount === 1 ? "" : "s"} · ${hiddenCount} hidden test${hiddenCount === 1 ? "" : "s"} on submit</p>
        </div>
        ${hints.length ? `
        <div class="ws-pane" data-pane="hints" hidden>
          <p class="hints-intro">Stuck? Open one hint at a time. Each one gives away a little more of the approach.</p>
          ${hints.map((h, i) => `
            <details class="hint-card">
              <summary>${icon("chevron", 14)} Hint ${i + 1}</summary>
              <div class="prose">${markdown(h)}</div>
            </details>`).join("")}
        </div>` : ""}
        ${exam ? "" : `
        <div class="ws-pane" data-pane="sol" hidden>
          <div class="reveal-box">
            <p><strong>Try it yourself first.</strong> The reference solution is one way to solve it, written in the course's style.</p>
            <button class="btn" type="button" data-act="reveal">${icon("lock", 14)} Show reference solution</button>
          </div>
          <pre class="solution-code" hidden><code class="language-python">${esc(problem.solution)}</code></pre>
        </div>`}
      </section>

      <section class="ws-right" aria-label="Your code">
        <div class="ws-toolbar">
          <span class="file">${icon("code", 14)} solution.py</span>
          <span class="py-version">Python 3.12</span>
          <span class="spacer"></span>
          <button class="btn btn-sm btn-ghost" type="button" data-act="fullscreen"></button>
          <button class="btn btn-sm btn-ghost" type="button" data-act="reset" title="Replace your code with the starter code">${icon("reset", 14)} Reset</button>
        </div>
        <div class="ws-editor"></div>
        <div class="ws-actions">
          <span class="ws-status" aria-live="polite"></span>
          <span class="spacer"></span>
          <button class="btn" type="button" data-act="run" title="${MOD}+Enter">${icon("play", 14)} Run samples</button>
          <button class="btn btn-primary" type="button" data-act="submit" title="${MOD}+Shift+Enter">${icon("upload", 14)} Submit</button>
        </div>
        <div class="ws-results" aria-live="polite">
          <p class="muted empty-results">Run the sample tests (${MOD}+Enter) or submit against every test (${MOD}+Shift+Enter).</p>
        </div>
      </section>
    </div>`;

  highlightCode(root.querySelector(".ws-left"));

  const statusEl = root.querySelector(".ws-status");
  const resultsEl = root.querySelector(".ws-results");
  const buttons = [...root.querySelectorAll('[data-act="run"], [data-act="submit"]')];
  let busy = false;
  let saveTimer = null;

  const editor = createEditor(root.querySelector(".ws-editor"), initialCode, {
    onChange(value) {
      clearTimeout(saveTimer);
      saveTimer = setTimeout(() => store.set(opts.codeKey, value), 300);
    },
    onRun: () => go("run"),
    onSubmit: () => go("submit"),
  });

  // Tabs on the left
  root.querySelectorAll(".ws-tab").forEach((tab) => {
    tab.addEventListener("click", () => {
      root.querySelectorAll(".ws-tab").forEach((t) => t.classList.toggle("is-active", t === tab));
      root.querySelectorAll(".ws-left .ws-pane").forEach((p) => (p.hidden = p.dataset.pane !== tab.dataset.pane));
    });
  });

  root.querySelector('[data-act="reveal"]')?.addEventListener("click", (e) => {
    const pre = root.querySelector(".solution-code");
    pre.hidden = false;
    highlightCode(pre.parentElement);
    e.currentTarget.closest(".reveal-box").remove();
  });

  root.querySelector('[data-act="reset"]').addEventListener("click", () => {
    if (!confirm("Replace your code with the starter code? Your current code will be lost.")) return;
    editor.set(problem.starter);
    store.set(opts.codeKey, problem.starter);
  });

  // Full screen: the workspace (or, in an exam, the whole exam screen with its timer) covers the window.
  const fsTarget = opts.fullscreenTarget || root.querySelector(".ws");
  const fsButton = root.querySelector('[data-act="fullscreen"]');
  const setFullscreen = (on) => {
    fullscreenOn = on;
    fsTarget.classList.toggle("is-fullscreen", on);
    document.body.classList.toggle("has-fullscreen", on);
    fsButton.title = on ? "Exit full screen (Esc)" : "Full screen";
    fsButton.setAttribute("aria-label", on ? "Exit full screen" : "Full screen");
    fsButton.innerHTML = `${icon(on ? "collapse" : "expand", 14)} <span class="btn-label">${on ? "Exit full screen" : "Full screen"}</span>`;
    requestAnimationFrame(() => editor.refresh());
  };
  fsButton.addEventListener("click", () => setFullscreen(!fullscreenOn));
  const onKey = (e) => {
    if (e.key === "Escape" && fullscreenOn) setFullscreen(false);
  };
  document.addEventListener("keydown", onKey);
  setFullscreen(fullscreenOn);

  root.querySelector('[data-act="run"]').addEventListener("click", () => go("run"));
  root.querySelector('[data-act="submit"]').addEventListener("click", () => go("submit"));

  const stopListening = onJudgeState((state, detail) => {
    if (busy) return;
    statusEl.innerHTML = {
      idle: "",
      loading: `<span class="spinner"></span> Loading Python (first time only, about 10 MB)…`,
      ready: `<span class="ok-dot"></span> Python ready`,
      error: `Python couldn't load. Check your connection and reload. ${esc(detail)}`,
    }[state];
  });
  warmUp();

  if (opts.lastOutcome) renderOutcome(resultsEl, opts.lastOutcome, exam);

  async function go(runMode) {
    if (busy) return;
    busy = true;
    buttons.forEach((b) => (b.disabled = true));
    store.set(opts.codeKey, editor.get());
    resultsEl.innerHTML = `<p class="muted"><span class="spinner"></span> Starting…</p>`;
    const outcome = await judge({
      code: editor.get(),
      problem,
      mode: runMode,
      onProgress(i, n) {
        statusEl.innerHTML = `<span class="spinner"></span> Running test ${i} of ${n}…`;
        resultsEl.innerHTML = `<p class="muted"><span class="spinner"></span> Running test ${i} of ${n}…</p>`;
      },
    });
    outcome.mode = runMode;
    renderOutcome(resultsEl, outcome, exam);
    busy = false;
    buttons.forEach((b) => (b.disabled = false));
    statusEl.innerHTML = `<span class="ok-dot"></span> Python ready`;
    opts.onResult?.(outcome, runMode);
  }

  const onResize = () => editor.refresh();
  window.addEventListener("resize", onResize);
  requestAnimationFrame(() => editor.refresh());

  return () => {
    clearTimeout(saveTimer);
    store.set(opts.codeKey, editor.get());
    stopListening();
    window.removeEventListener("resize", onResize);
    document.removeEventListener("keydown", onKey);
    fsTarget.classList.remove("is-fullscreen");
    document.body.classList.remove("has-fullscreen");
  };
}

// ---- results ---------------------------------------------------------------------

function renderOutcome(el, outcome, exam) {
  const v = VERDICTS[outcome.verdict] || VERDICTS.internal;
  const passed = outcome.results.filter((r) => r.status === "passed").length;
  const total = outcome.results.length;
  const scope = outcome.mode === "submit" ? "tests" : "sample tests";

  if (outcome.verdict === "compile_error" || outcome.verdict === "unavailable" || (outcome.verdict === "internal" && !total)) {
    el.innerHTML = `
      <div class="verdict tone-${v.tone}">${icon(outcome.verdict === "compile_error" ? "x" : "clock", 18)} ${v.text}</div>
      <pre class="out out-error">${esc(outcome.message)}</pre>`;
    return;
  }

  let openedOne = false;
  const rows = outcome.results.map((r) => {
    const s = STATUS[r.status] || STATUS.internal;
    const hidden = r.test.hidden;
    const label = hidden ? `Hidden test ${r.index + 1}` : esc(r.test.name || `Test ${r.index + 1}`);
    const open = !openedOne && r.status !== "passed" && r.status !== "skipped";
    if (open) openedOne = true;
    return `
      <details class="test tone-${s.tone}" ${open ? "open" : ""}>
        <summary>
          <span class="test-icon">${icon(s.icon, 14)}</span>
          <span class="test-name">${label}</span>
          <span class="test-status">${s.text}</span>
          ${r.ms != null && r.status !== "skipped" ? `<span class="test-ms">${r.ms} ms</span>` : ""}
        </summary>
        <div class="test-body">${hidden ? hiddenBody(r, exam) : visibleBody(r)}</div>
      </details>`;
  });

  el.innerHTML = `
    <div class="verdict tone-${v.tone}">
      ${icon(outcome.verdict === "accepted" ? "check" : outcome.verdict === "tle" ? "clock" : "x", 18)}
      <span>${v.text}</span>
      <span class="verdict-count">${passed} / ${total} ${scope} passed</span>
    </div>
    ${outcome.verdict === "accepted" && outcome.mode === "run" ? `<p class="muted small">Samples pass. Submit to run the hidden tests too.</p>` : ""}
    <div class="tests">${rows.join("")}</div>`;
}

function visibleBody(r) {
  const input = [r.test.data, r.test.setup, r.test.expr].filter(Boolean).join("\n");
  return `
    <div class="kv"><span>Input</span><pre class="out">${esc(input)}</pre></div>
    ${r.status === "skipped" ? "" : `
    ${r.expected != null ? `<div class="kv"><span>Expected</span><pre class="out">${esc(r.expected)}</pre></div>` : ""}
    ${r.actual != null ? `<div class="kv"><span>Your output</span><pre class="out">${esc(r.actual)}</pre></div>` : ""}
    ${r.stdout ? `<div class="kv"><span>Printed</span><pre class="out">${esc(r.stdout)}</pre></div>` : ""}
    ${r.error ? `<div class="kv"><span>Error</span><pre class="out out-error">${esc(r.error)}</pre></div>` : ""}`}`;
}

function hiddenBody(r, exam) {
  if (r.status === "passed") return `<p class="muted small">Input hidden.</p>`;
  if (r.status === "skipped") return `<p class="muted small">Not run because an earlier test ran out of time.</p>`;
  const lastLine = (r.error || "").trim().split("\n").pop();
  return `
    <p class="muted small">Input hidden.${exam ? "" : ` Test name: <em>${esc(r.test.name)}</em>`}</p>
    ${r.status === "runtime_error" || r.status === "tle" ? `<pre class="out out-error">${esc(lastLine)}</pre>` : ""}
    ${!exam && r.test.hint ? `
    <details class="hint">
      <summary>${icon("flag", 14)} Show a hint for this test</summary>
      <p>${esc(r.test.hint)}</p>
    </details>` : ""}`;
}

// ---- editor -----------------------------------------------------------------------

const INDENT = 4;

// Backspace inside a line's leading spaces deletes back to the previous 4-column stop,
// so one Backspace undoes one Tab. Anywhere else it deletes one character as usual.
function backspaceIndent(ed) {
  const ranges = ed.listSelections();
  const cuts = [];
  for (const r of ranges) {
    const { line, ch } = r.head;
    if (!r.empty() || ch === 0 || !/^ +$/.test(ed.getLine(line).slice(0, ch))) return window.CodeMirror.Pass;
    cuts.push({ line, from: ch - (((ch - 1) % INDENT) + 1), to: ch });
  }
  ed.operation(() => {
    for (const c of cuts.reverse()) ed.replaceRange("", { line: c.line, ch: c.from }, { line: c.line, ch: c.to }, "+delete");
  });
}

function createEditor(host, value, { onChange, onRun, onSubmit }) {
  if (window.CodeMirror) {
    const cm = window.CodeMirror(host, {
      value,
      mode: "python",
      lineNumbers: true,
      indentUnit: INDENT,
      tabSize: INDENT,
      indentWithTabs: false,
      matchBrackets: true,
      autoCloseBrackets: true,
      viewportMargin: 30,
      extraKeys: {
        Tab: (ed) => (ed.somethingSelected() ? ed.indentSelection("add") : ed.execCommand("insertSoftTab")),
        "Shift-Tab": (ed) => ed.indentSelection("subtract"),
        Backspace: backspaceIndent,
        "Ctrl-Enter": onRun,
        "Cmd-Enter": onRun,
        "Shift-Ctrl-Enter": onSubmit,
        "Shift-Cmd-Enter": onSubmit,
        "Ctrl-/": "toggleComment",
        "Cmd-/": "toggleComment",
      },
    });
    cm.on("change", () => onChange(cm.getValue()));
    return { get: () => cm.getValue(), set: (v) => cm.setValue(v), refresh: () => cm.refresh() };
  }
  // Fallback if the editor library didn't load: a plain text box.
  const ta = document.createElement("textarea");
  ta.className = "plain-editor";
  ta.spellcheck = false;
  ta.value = value;
  ta.addEventListener("input", () => onChange(ta.value));
  ta.addEventListener("keydown", (e) => {
    const start = ta.selectionStart;
    const lineStart = start ? ta.value.lastIndexOf("\n", start - 1) + 1 : 0;
    if (e.key === "Tab") {
      e.preventDefault();
      ta.setRangeText(" ".repeat(INDENT - ((start - lineStart) % INDENT)), start, ta.selectionEnd, "end");
      onChange(ta.value);
    } else if (e.key === "Backspace" && start === ta.selectionEnd && start > lineStart && /^ +$/.test(ta.value.slice(lineStart, start))) {
      e.preventDefault();
      ta.setRangeText("", start - (((start - lineStart - 1) % INDENT) + 1), start, "end");
      onChange(ta.value);
    } else if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      (e.shiftKey ? onSubmit : onRun)();
    }
  });
  host.appendChild(ta);
  return { get: () => ta.value, set: (v) => { ta.value = v; }, refresh() {} };
}
