// Talks to the Pyodide worker: one message per test, each with a hard time limit.
// If a test runs past its limit (e.g. an infinite loop) the worker is killed and restarted.
const WORKER_URL = "js/judge-worker.js";
const DEFAULT_LIMIT_MS = 3000;

let worker = null;
let readyPromise = null;
let state = "idle"; // idle | loading | ready | error
let stateDetail = "";
let nextId = 1;
const pending = new Map();
const listeners = new Set();

function setState(next, detail = "") {
  state = next;
  stateDetail = detail;
  listeners.forEach((fn) => fn(state, stateDetail));
}

export function onJudgeState(fn) {
  listeners.add(fn);
  fn(state, stateDetail);
  return () => listeners.delete(fn);
}

function startWorker() {
  if (readyPromise) return readyPromise;
  setState("loading");
  worker = new Worker(WORKER_URL);
  readyPromise = new Promise((resolve, reject) => {
    worker.onmessage = ({ data }) => {
      if (data.type === "ready") {
        setState("ready");
        resolve();
      } else if (data.type === "load-error") {
        setState("error", data.error);
        reject(new Error(data.error));
      } else if (data.type === "result") {
        const done = pending.get(data.id);
        if (done) {
          pending.delete(data.id);
          done(data);
        }
      }
    };
    worker.onerror = (event) => {
      const message = event.message || "The Python worker crashed.";
      setState("error", message);
      reject(new Error(message));
    };
  });
  readyPromise.catch(() => {
    worker?.terminate();
    worker = null;
    readyPromise = null; // let the next run try again
  });
  return readyPromise;
}

function restartWorker() {
  worker?.terminate();
  worker = null;
  readyPromise = null;
  pending.clear();
  startWorker().catch(() => {});
}

/** Start downloading Python in the background (call when a code editor appears). */
export function warmUp() {
  startWorker().catch(() => {});
}

function send(message, timeoutMs) {
  return new Promise((resolve) => {
    const id = nextId++;
    const timer = timeoutMs
      ? setTimeout(() => {
          pending.delete(id);
          restartWorker();
          resolve({ timedOut: true });
        }, timeoutMs)
      : null;
    pending.set(id, (data) => {
      clearTimeout(timer);
      resolve(data);
    });
    worker.postMessage({ ...message, id });
  });
}

const VERDICT_FOR_STATUS = {
  wrong: "wrong_answer",
  runtime_error: "runtime_error",
  tle: "tle",
  internal: "internal",
};

/**
 * Judge `code` against a problem's tests.
 * mode "run" uses only the visible tests; "submit" uses all of them.
 * Returns { verdict, message, results: [{ test, index, status, ms, actual, expected, stdout, error }] }.
 */
export async function judge({ code, problem, mode, onProgress }) {
  try {
    await startWorker();
  } catch (err) {
    return { verdict: "unavailable", message: String(err.message || err), results: [] };
  }

  const all = problem.tests.map((test, index) => ({ test, index }));
  const chosen = mode === "submit" ? all : all.filter(({ test }) => !test.hidden);

  const syntax = await send({ op: "syntax", code }, 10000);
  if (syntax.timedOut || syntax.error) {
    return { verdict: "internal", message: syntax.error || "The judge didn't respond.", results: [] };
  }
  if (syntax.out) return { verdict: "compile_error", message: syntax.out, results: [] };

  const results = [];
  for (let i = 0; i < chosen.length; i++) {
    const { test, index } = chosen[i];
    onProgress?.(i + 1, chosen.length);
    try {
      await startWorker(); // waits for a restart to finish so its load time isn't counted
    } catch (err) {
      return { verdict: "unavailable", message: String(err.message || err), results };
    }
    const limitMs = test.timeLimitMs || problem.timeLimitMs || DEFAULT_LIMIT_MS;
    const reply = await send(
      { op: "test", code, prelude: problem.prelude, checker: problem.checker, test, limitMs },
      limitMs * 2 + 2000,
    );
    if (reply.timedOut) {
      results.push({
        test, index, status: "tle", ms: limitMs,
        error: `Stopped after ${((limitMs * 2 + 2000) / 1000).toFixed(0)} s: the code is too slow or stuck in a loop.`,
      });
      for (const rest of chosen.slice(i + 1)) results.push({ ...rest, status: "skipped" });
      break;
    }
    if (reply.error) {
      results.push({ test, index, status: "internal", error: reply.error });
      continue;
    }
    results.push({ test, index, ...JSON.parse(reply.out) });
  }

  const firstBad = results.find((r) => r.status !== "passed");
  const verdict = firstBad ? VERDICT_FOR_STATUS[firstBad.status] || "internal" : "accepted";
  return { verdict, message: "", results };
}
