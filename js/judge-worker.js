/* Runs student code with Pyodide (Python compiled for the browser) inside a Web Worker.
   The page can terminate this worker if a program runs too long. */
const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
importScripts(PYODIDE_URL + "pyodide.js");

let pyodide = null;

const ready = (async () => {
  pyodide = await loadPyodide({ indexURL: PYODIDE_URL });
  const res = await fetch(new URL("../judge/harness.py", self.location.href));
  if (!res.ok) throw new Error(`Couldn't load the judge harness (${res.status})`);
  pyodide.runPython(await res.text());
})();

ready.then(
  () => self.postMessage({ type: "ready" }),
  (err) => self.postMessage({ type: "load-error", error: String(err) }),
);

self.onmessage = async ({ data }) => {
  const { id, op } = data;
  try {
    await ready;
    let out = null;
    if (op === "syntax") {
      const fn = pyodide.globals.get("check_syntax");
      out = fn(data.code) ?? null;
      fn.destroy();
    } else if (op === "test") {
      const fn = pyodide.globals.get("run_one");
      out = fn(data.code, data.prelude || "", data.checker || "", JSON.stringify(data.test), data.limitMs);
      fn.destroy();
    }
    self.postMessage({ type: "result", id, out });
  } catch (err) {
    self.postMessage({ type: "result", id, error: String(err) });
  }
};
