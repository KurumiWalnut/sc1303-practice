// Progress, drafts and exam attempts live in this browser only (localStorage).
// Every access is wrapped so the site still works when storage is blocked.
const PREFIX = "sc1303.v1.";

export const store = {
  get(key, fallback = null) {
    try {
      const raw = localStorage.getItem(PREFIX + key);
      return raw === null ? fallback : JSON.parse(raw);
    } catch {
      return fallback;
    }
  },
  set(key, value) {
    try {
      localStorage.setItem(PREFIX + key, JSON.stringify(value));
    } catch {
      /* storage full or blocked: progress just won't be remembered */
    }
  },
  remove(key) {
    try {
      localStorage.removeItem(PREFIX + key);
    } catch {
      /* ignore */
    }
  },
  removeWhere(test) {
    try {
      Object.keys(localStorage)
        .filter((k) => k.startsWith(PREFIX) && test(k.slice(PREFIX.length)))
        .forEach((k) => localStorage.removeItem(k));
    } catch {
      /* ignore */
    }
  },
};

// ---- practice progress -------------------------------------------------------

export function getProgress(problemId) {
  return store.get(`progress:${problemId}`, null);
}

export function recordSubmission(problemId, outcome) {
  const prev = getProgress(problemId) || {};
  const passed = outcome.results.filter((r) => r.status === "passed").length;
  const total = outcome.results.length;
  const solved = prev.solved || outcome.verdict === "accepted";
  const best = !prev.best || passed > prev.best.passed ? { passed, total } : prev.best;
  store.set(`progress:${problemId}`, { solved, best, lastVerdict: outcome.verdict, at: Date.now() });
}

export function problemState(problemId) {
  const p = getProgress(problemId);
  if (!p) return "new";
  return p.solved ? "solved" : "attempted";
}

// ---- exam attempts --------------------------------------------------------------

export function getAttempt(examId) {
  return store.get(`exam:${examId}`, null);
}

export function saveAttempt(examId, attempt) {
  store.set(`exam:${examId}`, attempt);
}

export function clearAttempt(examId) {
  store.remove(`exam:${examId}`);
  store.removeWhere((k) => k.startsWith(`examcode:${examId}:`));
}

export function resetEverything() {
  store.removeWhere(() => true);
}
