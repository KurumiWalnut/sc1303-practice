// Small shared helpers for building pages.

export const esc = (value) =>
  String(value ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

export function markdown(text) {
  if (window.marked) return window.marked.parse(text, { gfm: true });
  return `<pre>${esc(text)}</pre>`;
}

/** Syntax-highlight Python code blocks inside `root` (no-op if CodeMirror didn't load). */
export function highlightCode(root) {
  if (!window.CodeMirror?.runMode) return;
  root.querySelectorAll("pre > code").forEach((el) => {
    const lang = (el.className.match(/language-(\w+)/) || [])[1] || "python";
    if (!["python", "py"].includes(lang)) return;
    const text = el.textContent;
    el.textContent = "";
    window.CodeMirror.runMode(text, "python", el);
    el.parentElement.classList.add("cm-s-default");
  });
}

const PATHS = {
  check: '<path d="M5 12.5l4.5 4.5L19 7.5" />',
  x: '<path d="M6.5 6.5l11 11M17.5 6.5l-11 11" />',
  chevron: '<path d="M9 6l6 6-6 6" />',
  external: '<path d="M14 5h5v5M19 5l-8 8M10 6H6a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-4" />',
  clock: '<circle cx="12" cy="12" r="8" /><path d="M12 8v4.5l3 2" />',
  play: '<path d="M8 6l10 6-10 6z" />',
  upload: '<path d="M12 16V5M7 10l5-5 5 5M5 19h14" />',
  reset: '<path d="M5 12a7 7 0 1 0 2.1-5M5 4v4h4" />',
  book: '<path d="M5 5.5A1.5 1.5 0 0 1 6.5 4H19v14H6.5A1.5 1.5 0 0 0 5 19.5zM5 19.5A1.5 1.5 0 0 0 6.5 21H19" />',
  code: '<path d="M9 8l-4 4 4 4M15 8l4 4-4 4" />',
  puzzle: '<path d="M10 4h4v3a2 2 0 1 0 4 0h2v13H4V7h2a2 2 0 1 0 4 0z" />',
  flag: '<path d="M6 21V4M6 4h11l-2 4 2 4H6" />',
  search: '<circle cx="11" cy="11" r="6" /><path d="M20 20l-4.5-4.5" />',
  dot: '<circle cx="12" cy="12" r="3.5" fill="currentColor" />',
  lock: '<rect x="5" y="11" width="14" height="9" rx="2" /><path d="M8 11V8a4 4 0 0 1 8 0v3" />',
  expand: '<path d="M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5" />',
  collapse: '<path d="M9 4v5H4M20 9h-5V4M15 20v-5h5M4 15h5v5" />',
};

export function icon(name, size = 16) {
  return `<svg class="icon" viewBox="0 0 24 24" width="${size}" height="${size}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${PATHS[name] || ""}</svg>`;
}

/** Ring icon for a problem: new, attempted or solved. */
export function stateIcon(state) {
  const label = { new: "Not started", attempted: "Attempted", solved: "Solved" }[state];
  return `<span class="state state-${state}" title="${label}" aria-label="${label}">${state === "solved" ? icon("check", 11) : ""}</span>`;
}

export function difficultyChip(difficulty) {
  if (!difficulty) return "";
  return `<span class="chip diff-${difficulty.toLowerCase()}">${esc(difficulty)}</span>`;
}

export function leetcodeLink(problem) {
  const lc = problem.leetcode || (problem.lc ? { number: problem.lc, slug: problem.slug } : null);
  if (!lc) return "";
  const label = `LeetCode ${lc.number}`;
  if (!lc.slug) return `<span class="chip">${label}</span>`;
  return `<a class="chip chip-link" href="https://leetcode.com/problems/${esc(lc.slug)}/" target="_blank" rel="noopener">${label} ${icon("external", 12)}</a>`;
}

export function formatClock(ms) {
  const total = Math.max(0, Math.round(ms / 1000));
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  const pad = (n) => String(n).padStart(2, "0");
  return h ? `${h}:${pad(m)}:${pad(s)}` : `${pad(m)}:${pad(s)}`;
}
