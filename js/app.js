import { loadTree, loadExams, loadNotes, loadProblem, loadProblemMeta, indexTree, leafProblemIds, baseList } from "./content.js";
import { store, problemState, recordSubmission, getAttempt, saveAttempt, clearAttempt, resetEverything } from "./storage.js";
import { mountWorkspace } from "./workspace.js";
import { onJudgeState, warmUp } from "./judge.js";
import { esc, markdown, highlightCode, icon, stateIcon, difficultyChip, leetcodeLink, formatClock } from "./ui.js";

const app = document.getElementById("app");
let tree;
let examsData;
let idx;
let cleanups = [];
let renderToken = 0;

const onCleanup = (fn) => cleanups.push(fn);
const isCurrent = (token) => token === renderToken;

// ---- boot ----------------------------------------------------------------------------

async function boot() {
  setupHeader();
  try {
    [tree, examsData] = await Promise.all([loadTree(), loadExams()]);
    idx = indexTree(tree);
  } catch (err) {
    app.innerHTML = `
      <div class="page narrow">
        <h1>The course content didn't load</h1>
        <p>${esc(err.message)}</p>
        <p>If you opened <code>index.html</code> straight from your files, start a local web server instead:</p>
        <pre class="out">cd platform\npython3 -m http.server 8000</pre>
        <p>Then open <a href="http://localhost:8000">http://localhost:8000</a>.</p>
      </div>`;
    return;
  }
  window.addEventListener("hashchange", route);
  route();
}

function setupHeader() {
  const pill = document.getElementById("pyPill");
  const label = pill.querySelector(".label");
  onJudgeState((state) => {
    pill.dataset.state = state;
    label.textContent = {
      idle: "Python loads when you code",
      loading: "Loading Python…",
      ready: "Python ready",
      error: "Python failed to load",
    }[state];
  });
  document.getElementById("menuBtn").addEventListener("click", () => {
    document.getElementById("learn")?.classList.toggle("is-tree-open");
  });
}

// ---- routing -------------------------------------------------------------------------

function route() {
  cleanups.splice(0).forEach((fn) => {
    try {
      fn();
    } catch {
      /* ignore cleanup errors */
    }
  });
  const token = ++renderToken;
  const [section = "", ...rest] = location.hash
    .replace(/^#\/?/, "")
    .split("/")
    .filter(Boolean)
    .map(decodeURIComponent);

  document.body.dataset.route = section || "home";
  document.querySelectorAll("[data-nav]").forEach((a) => a.classList.toggle("is-active", a.dataset.nav === section));

  const run = (promise) =>
    Promise.resolve(promise).catch((err) => {
      if (!isCurrent(token)) return;
      console.error(err);
      app.innerHTML = `<div class="page narrow"><h1>Something went wrong</h1><p>${esc(err.message || err)}</p><p><a href="#/">Back to the home page</a></p></div>`;
    });

  if (!section) return run(renderHome());
  if (section === "learn") return run(renderLearn(token, rest[0], rest[1], rest[2]));
  if (section === "exams") {
    if (!rest[0]) return run(renderExamList());
    return run(renderExam(token, rest[0], rest[1] === "q" ? Number(rest[2]) : null));
  }
  return run(renderNotFound());
}

function setTitle(text) {
  document.title = text ? `${text} · SC1303 Practice` : "SC1303 Practice";
}

function renderNotFound() {
  setTitle("Not found");
  app.innerHTML = `<div class="page narrow"><h1>Page not found</h1><p><a href="#/">Go to the home page</a></p></div>`;
}

// ---- progress helpers ---------------------------------------------------------------

function leafState(leaf) {
  const states = leafProblemIds(leaf).map(problemState);
  if (states.length && states.every((s) => s === "solved")) return "solved";
  if (states.some((s) => s !== "new")) return "attempted";
  return "new";
}

function leafSolvedCount(leaf) {
  const ids = leafProblemIds(leaf);
  return { solved: ids.filter((id) => problemState(id) === "solved").length, total: ids.length };
}

function examScore(exam, attempt) {
  const per = examsData.marksPerQuestion;
  let score = 0;
  for (const pid of exam.problems) {
    const best = attempt?.best?.[pid];
    if (best) score += Math.round((per * best.passed) / best.total);
  }
  return score;
}

// ---- home ----------------------------------------------------------------------------

function renderHome() {
  setTitle("");
  const solved = idx.readyProblems.filter((id) => problemState(id) === "solved").length;
  const bestMock = examsData.exams
    .filter((e) => e.status === "ready")
    .map((e) => ({ e, a: getAttempt(e.id) }))
    .filter(({ a }) => a?.finishedAt)
    .map(({ e, a }) => examScore(e, a));
  const firstReady = idx.ready[0];

  app.innerHTML = `
    <div class="page">
      <section class="hero">
        <p class="eyebrow">SC1303 · Weeks 5–12</p>
        <h1>Practise data structures the way you'll be tested.</h1>
        <p class="lead">Short notes, the base implementations from the course templates, and LeetCode-style problems, all checked by a Python judge that runs in your browser. Then sit a timed mock in the final quiz format: 4 questions in 90 minutes.</p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="#/learn/${esc(firstReady)}">Start learning</a>
          <a class="btn btn-lg" href="#/exams">Try a mock exam</a>
        </div>
      </section>

      <section class="stats" aria-label="Your progress">
        <div class="stat"><div class="num">${solved}<span>/${idx.readyProblems.length}</span></div><div class="label">problems solved</div></div>
        <div class="stat"><div class="num">${idx.ready.length}<span>/${idx.order.length}</span></div><div class="label">subtopics ready</div></div>
        <div class="stat"><div class="num">${bestMock.length ? `${Math.max(...bestMock)}<span>/100</span>` : "–"}</div><div class="label">best mock score</div></div>
      </section>

      <section class="section">
        <h2>Subtopics</h2>
        <div class="card-grid">${idx.ready.map(leafCard).join("")}</div>
      </section>

      <section class="section">
        <h2>How it works</h2>
        <ol class="steps">
          <li><strong>Pick a subtopic</strong> from the Learn tree. Topics follow the lecture order, from arrays in Week 5 to Dijkstra in Week 12.</li>
          <li><strong>Read the notes</strong>, then write the <strong>base implementation</strong>: the core code you should be able to write from memory.</li>
          <li><strong>Solve LeetCode-style problems.</strong> <em>Run samples</em> checks the examples; <em>Submit</em> also runs hidden tests, including large ones that catch slow solutions.</li>
          <li><strong>Sit a mock exam</strong> under time pressure, then compare your code with the reference solutions.</li>
        </ol>
      </section>

      ${siteFooter()}
    </div>`;
  bindFooter();
}

function leafCard(id) {
  const { leaf, topic } = idx.leaves.get(id);
  const { solved, total } = leafSolvedCount(leaf);
  return `
    <a class="leaf-card" href="#/learn/${esc(id)}">
      <span class="eyebrow">${esc(topic.title)} · Week ${esc(topic.week)}</span>
      <span class="leaf-card-title">${stateIcon(leafState(leaf))} ${esc(leaf.title)}</span>
      <span class="leaf-card-summary">${esc(leaf.summary)}</span>
      <span class="leaf-card-foot">${total} problems · ${solved} solved</span>
    </a>`;
}

function siteFooter() {
  return `
    <footer class="site-footer">
      <p>Unofficial study tool by SC1303 students; not affiliated with the course team. Problem statements are written for this site, and LeetCode links point to the original problems.</p>
      <p>Your progress and code are saved in this browser only. <button class="link-btn" type="button" data-act="reset-all">Reset my progress</button></p>
    </footer>`;
}

function bindFooter() {
  app.querySelector('[data-act="reset-all"]')?.addEventListener("click", () => {
    if (!confirm("Delete all your saved code, progress and mock exam attempts in this browser? This can't be undone.")) return;
    resetEverything();
    route();
  });
}

// ---- learn: tree ---------------------------------------------------------------------

function defaultOpenTopics() {
  return tree.parts.flatMap((p) => p.topics).filter((t) => t.leaves.some((l) => l.status === "ready")).map((t) => t.id);
}

function openTopics() {
  return new Set(store.get("ui:openTopics", null) ?? defaultOpenTopics());
}

function treeHTML(currentId) {
  const open = openTopics();
  if (currentId && idx.leaves.has(currentId)) open.add(idx.leaves.get(currentId).topic.id);
  return `
    <div class="tree-search">
      ${icon("search", 14)}
      <input type="search" placeholder="Filter subtopics" aria-label="Filter subtopics" autocomplete="off">
    </div>
    <a class="tree-home ${currentId ? "" : "is-current"}" href="#/learn">All topics</a>
    ${tree.parts
      .map(
        (part) => `
      <div class="tree-part">
        <div class="tree-part-title"><span>${esc(part.title)}</span><span>${esc(part.weeks)}</span></div>
        ${part.topics.map((topic) => topicHTML(topic, open.has(topic.id), currentId)).join("")}
      </div>`,
      )
      .join("")}
    <p class="tree-legend">
      <span>${stateIcon("solved")} solved</span>
      <span>${stateIcon("attempted")} tried</span>
      <span><span class="badge-soon">soon</span> planned</span>
    </p>`;
}

function topicHTML(topic, isOpen, currentId) {
  return `
    <div class="tree-topic ${isOpen ? "is-open" : ""}" data-topic="${esc(topic.id)}">
      <button class="tree-topic-btn" type="button" aria-expanded="${isOpen}">
        ${icon("chevron", 14)}
        <span class="tree-topic-title">${esc(topic.title)}</span>
        <span class="tree-week">W${esc(topic.week)}</span>
      </button>
      <ul class="tree-leaves">
        ${topic.leaves.map((leaf) => leafRowHTML(leaf, currentId)).join("")}
      </ul>
    </div>`;
}

function leafRowHTML(leaf, currentId) {
  const ready = leaf.status === "ready";
  const { solved, total } = leafSolvedCount(leaf);
  return `
    <li class="tree-leaf ${ready ? "" : "is-planned"}" data-title="${esc(leaf.title.toLowerCase())}">
      <a href="#/learn/${esc(leaf.id)}" class="${leaf.id === currentId ? "is-current" : ""}" ${leaf.id === currentId ? 'aria-current="page"' : ""}>
        ${ready ? stateIcon(leafState(leaf)) : '<span class="state state-planned" aria-hidden="true"></span>'}
        <span class="leaf-title">${esc(leaf.title)}</span>
        ${ready ? `<span class="leaf-meta">${solved}/${total}</span>` : `<span class="badge-soon">soon</span>`}
      </a>
    </li>`;
}

function bindTree(sidebar, currentId) {
  sidebar.addEventListener("click", (e) => {
    const btn = e.target.closest(".tree-topic-btn");
    if (btn) {
      const topicEl = btn.closest(".tree-topic");
      const nowOpen = !topicEl.classList.contains("is-open");
      topicEl.classList.toggle("is-open", nowOpen);
      btn.setAttribute("aria-expanded", nowOpen);
      const open = openTopics();
      nowOpen ? open.add(topicEl.dataset.topic) : open.delete(topicEl.dataset.topic);
      store.set("ui:openTopics", [...open]);
      return;
    }
    if (e.target.closest("a")) document.getElementById("learn")?.classList.remove("is-tree-open");
  });
  const input = sidebar.querySelector(".tree-search input");
  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    sidebar.querySelector(".tree").classList.toggle("is-filtering", Boolean(q));
    sidebar.querySelectorAll(".tree-topic").forEach((topicEl) => {
      const topicTitle = topicEl.querySelector(".tree-topic-title").textContent.toLowerCase();
      let any = false;
      topicEl.querySelectorAll(".tree-leaf").forEach((li) => {
        const match = !q || li.dataset.title.includes(q) || topicTitle.includes(q);
        li.hidden = !match;
        any ||= match;
      });
      topicEl.hidden = !any;
    });
  });
  // Keep the current subtopic in view.
  const current = sidebar.querySelector(".tree-leaf a.is-current");
  if (current && currentId) current.scrollIntoView({ block: "nearest" });
}

function refreshTree(currentId) {
  const sidebar = document.getElementById("sidebar");
  if (!sidebar) return;
  sidebar.querySelectorAll(".tree-leaf").forEach((li) => {
    const id = li.querySelector("a").getAttribute("href").split("/").pop();
    const entry = idx.leaves.get(id);
    if (!entry || entry.leaf.status !== "ready") return;
    li.outerHTML = leafRowHTML(entry.leaf, currentId);
  });
}

// ---- learn: pages --------------------------------------------------------------------

async function renderLearn(token, leafId, tab, pid) {
  const oldScroll = document.getElementById("sidebar")?.scrollTop ?? 0;
  app.innerHTML = `
    <div class="learn" id="learn">
      <aside class="sidebar" id="sidebar" aria-label="Topics"><nav class="tree">${treeHTML(leafId)}</nav></aside>
      <div class="scrim" id="scrim"></div>
      <section class="learn-main" id="learnMain"></section>
    </div>`;
  const sidebar = document.getElementById("sidebar");
  sidebar.scrollTop = oldScroll;
  bindTree(sidebar, leafId);
  document.getElementById("scrim").addEventListener("click", () => document.getElementById("learn").classList.remove("is-tree-open"));

  const main = document.getElementById("learnMain");
  if (!leafId) return renderLearnOverview(main);
  const entry = idx.leaves.get(leafId);
  if (!entry) {
    setTitle("Not found");
    main.innerHTML = `<div class="page narrow"><h1>Subtopic not found</h1><p><a href="#/learn">See all topics</a></p></div>`;
    return;
  }
  return renderLeaf(token, main, entry, tab, pid);
}

function renderLearnOverview(main) {
  setTitle("Learn");
  main.innerHTML = `
    <div class="page page-wide">
      <h1>Topics</h1>
      <p class="lead">Weeks 5 to 12, in lecture order. Each subtopic has notes, a base implementation question (if there is one) and LeetCode-style practice.</p>
      ${tree.parts
        .map(
          (part) => `
        <section class="section">
          <h2>${esc(part.title)} <span class="muted h-sub">${esc(part.weeks)}</span></h2>
          <div class="topic-grid">
            ${part.topics
              .map(
                (topic) => `
              <div class="topic-card">
                <div class="topic-card-head"><h3>${esc(topic.title)}</h3><span class="chip">Week ${esc(topic.week)}</span></div>
                <ul>
                  ${topic.leaves
                    .map((leaf) => {
                      const ready = leaf.status === "ready";
                      const { solved, total } = leafSolvedCount(leaf);
                      return `<li class="${ready ? "" : "is-planned"}"><a href="#/learn/${esc(leaf.id)}">
                        ${ready ? stateIcon(leafState(leaf)) : '<span class="state state-planned" aria-hidden="true"></span>'}
                        <span>${esc(leaf.title)}</span>
                        ${ready ? `<span class="leaf-meta">${solved}/${total}</span>` : `<span class="badge-soon">soon</span>`}
                      </a></li>`;
                    })
                    .join("")}
                </ul>
              </div>`,
              )
              .join("")}
          </div>
        </section>`,
        )
        .join("")}
    </div>`;
}

async function renderLeaf(token, main, entry, tab, pid) {
  const { leaf, topic, part } = entry;
  const ready = leaf.status === "ready";
  const current = ["notes", "implement", "practice"].includes(tab) ? tab : "notes";
  const practiceCount = (leaf.practice || []).length;
  const baseCount = baseList(leaf).length;
  const { solved, total } = leafSolvedCount(leaf);
  setTitle(leaf.title);

  const tabLink = (name, label, ic, count) => `
    <a class="tab ${name === current ? "is-active" : ""}" href="#/learn/${esc(leaf.id)}${name === "notes" ? "" : `/${name}`}" ${name === current ? 'aria-current="page"' : ""}>
      ${icon(ic, 15)} ${label}${count != null ? `<span class="count">${count}</span>` : ""}
    </a>`;

  main.innerHTML = `
    <header class="leaf-head">
      <div class="crumbs"><a href="#/learn">${esc(part.title)}</a> <span aria-hidden="true">›</span> <span>${esc(topic.title)}</span></div>
      <div class="leaf-title-row">
        <h1>${esc(leaf.title)}</h1>
        <span class="chip">Week ${esc(topic.week)}</span>
        ${ready ? `<span class="chip chip-ok" id="solvedChip">${solved} / ${total} solved</span>` : `<span class="chip chip-planned">Coming soon</span>`}
      </div>
      <p class="leaf-summary">${esc(leaf.summary || "")}</p>
      <nav class="tabs" aria-label="Sections">
        ${tabLink("notes", "Notes", "book")}
        ${tabLink("implement", "Base implementation", "code", baseCount > 1 ? baseCount : baseCount ? null : "–")}
        ${tabLink("practice", "LeetCode-style", "puzzle", practiceCount)}
      </nav>
    </header>
    <div class="leaf-body" id="leafBody"></div>`;

  const body = main.querySelector("#leafBody");
  if (current === "notes") return renderNotesTab(token, body, leaf);
  if (current === "implement") return renderImplementTab(token, body, leaf, pid);
  return renderPracticeTab(token, body, leaf, pid);
}

async function renderNotesTab(token, body, leaf) {
  const nextLink = leaf.base
    ? `<a class="btn" href="#/learn/${esc(leaf.id)}/implement">Next: base implementation ${icon("chevron", 14)}</a>`
    : leaf.practice?.length
      ? `<a class="btn" href="#/learn/${esc(leaf.id)}/practice">Next: LeetCode-style practice ${icon("chevron", 14)}</a>`
      : "";

  if (leaf.status !== "ready") {
    body.innerHTML = `
      <div class="wire">
        <span class="wire-label">Notes · coming soon</span>
        <p>These notes will cover:</p>
        <ul>${(leaf.outline || []).map((o) => `<li>${esc(o)}</li>`).join("")}</ul>
        <div class="wire-lines" aria-hidden="true"><span></span><span></span><span class="short"></span><span></span><span class="short"></span></div>
      </div>
      <p class="contribute">Want to write these notes? They're Markdown files in <code>content/notes/</code>; see the README.</p>
      <div class="next-row">${nextLink}</div>`;
    return;
  }

  body.innerHTML = `<p class="muted">Loading notes…</p>`;
  const text = await loadNotes(leaf.notes);
  if (!isCurrent(token)) return;
  body.innerHTML = `<article class="prose notes">${markdown(text)}</article><div class="next-row">${nextLink}</div>`;
  highlightCode(body);
}

function workspaceSkeleton(title, note) {
  return `
    <div class="wire wire-ws">
      <span class="wire-label">${esc(note)}</span>
      <div class="wire-ws-grid" aria-hidden="true">
        <div class="wire-pane">
          <strong>${esc(title)}</strong>
          <div class="wire-lines"><span></span><span></span><span class="short"></span><span></span><span class="short"></span><span></span></div>
        </div>
        <div class="wire-pane wire-editor">
          <div class="wire-code"><span style="width:55%"></span><span style="width:70%"></span><span style="width:40%"></span><span style="width:62%"></span><span style="width:30%"></span></div>
          <div class="wire-buttons"><span class="btn btn-sm" disabled>Run samples</span><span class="btn btn-sm btn-primary" disabled>Submit</span></div>
          <div class="wire-results">Test results</div>
        </div>
      </div>
    </div>`;
}

async function renderImplementTab(token, body, leaf, pid) {
  const items = baseList(leaf);
  if (!items.length) {
    body.innerHTML = `
      <div class="empty">
        <h2>No base implementation here</h2>
        <p>This subtopic is about ideas rather than one piece of code to memorise.</p>
        ${leaf.practice?.length ? `<a class="btn" href="#/learn/${esc(leaf.id)}/practice">Go to LeetCode-style practice</a>` : ""}
      </div>`;
    return;
  }
  // Several base implementations (e.g. Lomuto and Hoare) get a picker like the practice tab.
  if (items.length > 1) return renderProblemList(token, body, leaf, "implement", items, pid, "Base implementation · coming soon");
  if (typeof items[0] !== "string") {
    body.innerHTML = workspaceSkeleton(items[0].title, "Base implementation · coming soon");
    return;
  }
  body.classList.add("is-workspace");
  body.innerHTML = `<p class="muted">Loading problem…</p>`;
  const problem = await loadProblem(items[0]);
  if (!isCurrent(token)) return;
  mountProblem(body, problem, leaf);
}

async function renderPracticeTab(token, body, leaf, pid) {
  const items = leaf.practice || [];
  if (!items.length) {
    body.innerHTML = `
      <div class="empty">
        <h2>No LeetCode-style problems here</h2>
        <p>Practise this subtopic with the base implementation instead.</p>
        ${leaf.base ? `<a class="btn" href="#/learn/${esc(leaf.id)}/implement">Go to the base implementation</a>` : ""}
      </div>`;
    return;
  }
  return renderProblemList(token, body, leaf, "practice", items, pid, "LeetCode-style problems · coming soon");
}

/** A row of problem picks (ready or planned) above the selected problem's workspace. */
async function renderProblemList(token, body, leaf, tab, items, pid, soonNote) {
  const readyIds = items.filter((p) => typeof p === "string");
  const metas = await Promise.all(readyIds.map(loadProblemMeta));
  if (!isCurrent(token)) return;
  const metaById = Object.fromEntries(metas.map((m) => [m.id, m]));
  const selected = readyIds.includes(pid) ? pid : readyIds[0];

  const picker = items
    .map((p) => {
      if (typeof p === "string") {
        const m = metaById[p];
        return `
          <a class="pick ${p === selected ? "is-active" : ""}" data-pid="${esc(p)}" href="#/learn/${esc(leaf.id)}/${tab}/${esc(p)}">
            <span class="pick-state">${stateIcon(problemState(p))}</span>
            <span>${esc(m.title)}</span>
            ${difficultyChip(m.difficulty)}
          </a>`;
      }
      return `
        <span class="pick is-planned" title="Coming soon">
          <span class="state state-planned" aria-hidden="true"></span>
          <span>${esc(p.title)}</span>
          ${difficultyChip(p.difficulty)}
          ${p.lc ? leetcodeLink(p) : p.source ? `<span class="chip">${esc(p.source)}</span>` : ""}
          <span class="badge-soon">soon</span>
        </span>`;
    })
    .join("");

  if (!selected) {
    body.innerHTML = `
      <div class="picker" role="list">${picker}</div>
      ${workspaceSkeleton(items[0].title, soonNote)}`;
    return;
  }

  body.classList.add("is-workspace");
  body.innerHTML = `<div class="picker">${picker}</div><div class="ws-host" id="wsHost"><p class="muted">Loading problem…</p></div>`;
  const problem = await loadProblem(selected);
  if (!isCurrent(token)) return;
  mountProblem(body.querySelector("#wsHost"), problem, leaf);
}

function mountProblem(host, problem, leaf) {
  const cleanup = mountWorkspace(host, problem, {
    mode: "practice",
    codeKey: `code:${problem.id}`,
    onResult(outcome, runMode) {
      if (runMode !== "submit" || !["accepted", "wrong_answer", "runtime_error", "tle"].includes(outcome.verdict)) return;
      recordSubmission(problem.id, outcome);
      refreshTree(leaf.id);
      const chip = document.getElementById("solvedChip");
      if (chip) {
        const { solved, total } = leafSolvedCount(leaf);
        chip.textContent = `${solved} / ${total} solved`;
      }
      document.querySelectorAll(`.pick[data-pid="${problem.id}"] .pick-state`).forEach((el) => {
        el.innerHTML = stateIcon(problemState(problem.id));
      });
    },
  });
  onCleanup(cleanup);
}

// ---- mock exams ------------------------------------------------------------------------

const RULES = `
  <ul class="rules-list">
    <li>Each question is worth ${25} marks, split evenly across its tests. Your best submission for each question counts.</li>
    <li><strong>Run samples</strong> as often as you like. <strong>Submit</strong> runs the hidden tests and updates your marks.</li>
    <li>No notes, hints or solutions until you finish. You can switch between questions at any time.</li>
    <li>The timer keeps running if you close the tab. When it reaches zero, the exam ends automatically.</li>
  </ul>`;

function renderExamList() {
  setTitle("Mock exams");
  const cards = examsData.exams
    .map((exam) => {
      if (exam.status !== "ready") {
        return `
          <div class="exam-card wire">
            <span class="wire-label">Coming soon</span>
            <h2>${esc(exam.title)}</h2>
            <p class="muted">4 questions · ${exam.durationMin} minutes</p>
            <p>Covers: ${exam.covers.map(esc).join(", ")}</p>
            <button class="btn" disabled>Not available yet</button>
          </div>`;
      }
      const attempt = getAttempt(exam.id);
      const endAt = attempt ? attempt.startedAt + exam.durationMin * 60000 : 0;
      let status = `<span class="chip">Not started</span>`;
      let action = `<a class="btn btn-primary" href="#/exams/${esc(exam.id)}">Start</a>`;
      if (attempt?.finishedAt) {
        status = `<span class="chip chip-ok">Score ${examScore(exam, attempt)} / ${exam.problems.length * examsData.marksPerQuestion}</span>`;
        action = `<a class="btn" href="#/exams/${esc(exam.id)}">View results</a>`;
      } else if (attempt) {
        status = `<span class="chip chip-warn">In progress · ${formatClock(endAt - Date.now())} left</span>`;
        action = `<a class="btn btn-primary" href="#/exams/${esc(exam.id)}/q/1">Resume</a>`;
      }
      return `
        <div class="exam-card">
          <div class="exam-card-top">${status}</div>
          <h2>${esc(exam.title)}</h2>
          <p class="muted">${exam.problems.length} questions · ${exam.durationMin} minutes · Python 3.12</p>
          <p>Covers: ${exam.covers.map(esc).join(", ")}</p>
          ${action}
        </div>`;
    })
    .join("");

  app.innerHTML = `
    <div class="page">
      <h1>Mock exams</h1>
      <p class="lead">The same format as the final coding quiz: 4 questions in 90 minutes, auto-judged with hidden tests.</p>
      <div class="exam-grid">${cards}</div>
      <section class="card rules"><h2>Rules</h2>${RULES}</section>
    </div>`;
}

async function renderExam(token, examId, q) {
  const exam = examsData.exams.find((e) => e.id === examId);
  if (!exam) return renderNotFound();
  setTitle(exam.title);
  if (exam.status !== "ready") {
    app.innerHTML = `<div class="page narrow"><a class="back" href="#/exams">← Mock exams</a><div class="wire"><span class="wire-label">Coming soon</span><h1>${esc(exam.title)}</h1><p>Covers: ${exam.covers.map(esc).join(", ")}</p></div></div>`;
    return;
  }

  let attempt = getAttempt(exam.id);
  if (attempt && !attempt.finishedAt && Date.now() >= attempt.startedAt + exam.durationMin * 60000) {
    attempt.finishedAt = attempt.startedAt + exam.durationMin * 60000;
    attempt.timedOut = true;
    saveAttempt(exam.id, attempt);
  }
  if (!attempt) return renderExamIntro(exam);
  if (attempt.finishedAt) return renderExamResults(token, exam, attempt);
  if (!q || q < 1 || q > exam.problems.length) {
    location.replace(`#/exams/${exam.id}/q/1`);
    return;
  }
  return renderExamRunner(token, exam, attempt, q);
}

function renderExamIntro(exam) {
  warmUp(); // download Python now so it's ready when the clock starts
  app.innerHTML = `
    <div class="page narrow">
      <a class="back" href="#/exams">← Mock exams</a>
      <h1>${esc(exam.title)}</h1>
      <p class="lead">${exam.problems.length} questions · ${exam.durationMin} minutes · Python 3.12</p>
      <section class="card">
        <p><strong>Covers:</strong> ${exam.covers.map(esc).join(", ")}</p>
        ${RULES}
      </section>
      <div class="start-row">
        <button class="btn btn-primary btn-lg" type="button" data-act="start">Start the ${exam.durationMin}-minute timer</button>
        <span class="muted small" id="introStatus"></span>
      </div>
    </div>`;
  const status = app.querySelector("#introStatus");
  onCleanup(
    onJudgeState((s) => {
      status.textContent = { idle: "", loading: "Loading Python in the background…", ready: "Python is ready.", error: "Python couldn't load. Check your connection." }[s];
    }),
  );
  app.querySelector('[data-act="start"]').addEventListener("click", () => {
    clearAttempt(exam.id);
    saveAttempt(exam.id, { startedAt: Date.now(), finishedAt: null, best: {}, submissions: {} });
    location.hash = `#/exams/${exam.id}/q/1`;
  });
}

async function renderExamRunner(token, exam, attempt, q) {
  const problems = await Promise.all(exam.problems.map(loadProblem));
  if (!isCurrent(token)) return;
  const per = examsData.marksPerQuestion;
  const qi = q - 1;
  const problem = problems[qi];
  const endAt = attempt.startedAt + exam.durationMin * 60000;

  const qScore = (pid) => {
    const best = attempt.best[pid];
    return best ? `${Math.round((per * best.passed) / best.total)}/${per}` : "–";
  };

  app.innerHTML = `
    <div class="exam">
      <div class="exam-bar">
        <div class="exam-name">
          <strong>${esc(exam.title)}</strong>
          <span class="muted small">Question ${q} of ${problems.length} · ${per} marks</span>
        </div>
        <nav class="qtabs" aria-label="Questions">
          ${problems
            .map(
              (p, i) => `
            <a class="qtab ${i === qi ? "is-active" : ""}" href="#/exams/${esc(exam.id)}/q/${i + 1}" ${i === qi ? 'aria-current="page"' : ""}>
              Q${i + 1} <span class="qscore" data-q="${esc(p.id)}">${qScore(p.id)}</span>
            </a>`,
            )
            .join("")}
        </nav>
        <span class="spacer"></span>
        <div class="timer" id="timer" role="timer" aria-label="Time left">${formatClock(endAt - Date.now())}</div>
        <button class="btn" type="button" data-act="finish">Finish exam</button>
      </div>
      <div class="exam-body" id="examBody"></div>
    </div>`;

  const finish = (timedOut) => {
    const latest = getAttempt(exam.id) || attempt;
    if (latest.finishedAt) return;
    latest.finishedAt = Math.min(Date.now(), endAt);
    latest.timedOut = Boolean(timedOut);
    saveAttempt(exam.id, latest);
    location.hash = `#/exams/${exam.id}`;
  };

  app.querySelector('[data-act="finish"]').addEventListener("click", () => {
    if (confirm("Finish the exam now? You can't change your answers afterwards.")) finish(false);
  });

  const timerEl = app.querySelector("#timer");
  const tick = () => {
    const left = endAt - Date.now();
    timerEl.textContent = formatClock(left);
    timerEl.classList.toggle("is-low", left < 10 * 60000 && left >= 2 * 60000);
    timerEl.classList.toggle("is-critical", left < 2 * 60000);
    if (left <= 0) finish(true);
  };
  tick();
  const interval = setInterval(tick, 1000);
  onCleanup(() => clearInterval(interval));

  const cleanup = mountWorkspace(app.querySelector("#examBody"), problem, {
    mode: "exam",
    codeKey: `examcode:${exam.id}:${problem.id}`,
    fullscreenTarget: app.querySelector(".exam"),
    onResult(outcome, runMode) {
      if (runMode !== "submit" || !outcome.results.length || outcome.verdict === "internal") return;
      const latest = getAttempt(exam.id);
      if (!latest || latest.finishedAt) return;
      const passed = outcome.results.filter((r) => r.status === "passed").length;
      const total = outcome.results.length;
      const prev = latest.best[problem.id];
      if (!prev || passed > prev.passed) latest.best[problem.id] = { passed, total };
      latest.submissions[problem.id] = (latest.submissions[problem.id] || 0) + 1;
      saveAttempt(exam.id, latest);
      attempt = latest;
      const el = app.querySelector(`.qscore[data-q="${problem.id}"]`);
      if (el) el.textContent = qScore(problem.id);
    },
  });
  onCleanup(cleanup);
}

async function renderExamResults(token, exam, attempt) {
  const problems = await Promise.all(exam.problems.map(loadProblem));
  if (!isCurrent(token)) return;
  const per = examsData.marksPerQuestion;
  const max = per * problems.length;
  const score = examScore(exam, attempt);
  const used = attempt.finishedAt - attempt.startedAt;

  const rows = problems
    .map((p, i) => {
      const best = attempt.best[p.id];
      const marks = best ? Math.round((per * best.passed) / best.total) : 0;
      return `
        <tr>
          <td>Q${i + 1}</td>
          <td>${esc(p.title)} <span class="muted small">· ${esc(p.difficulty)}</span></td>
          <td>${best ? `${best.passed} / ${best.total}` : "Not submitted"}</td>
          <td class="num-cell"><strong>${marks}</strong> / ${per}</td>
        </tr>`;
    })
    .join("");

  const reviews = problems
    .map((p, i) => {
      const code = store.get(`examcode:${exam.id}:${p.id}`) ?? p.starter;
      return `
        <details class="review">
          <summary><strong>Q${i + 1}. ${esc(p.title)}</strong> ${difficultyChip(p.difficulty)} ${leetcodeLink(p)}</summary>
          <div class="review-grid">
            <div><h4>Your code</h4><pre><code class="language-python">${esc(code)}</code></pre></div>
            <div><h4>Reference solution</h4><pre><code class="language-python">${esc(p.solution)}</code></pre></div>
          </div>
        </details>`;
    })
    .join("");

  app.innerHTML = `
    <div class="page">
      <a class="back" href="#/exams">← Mock exams</a>
      <h1>${esc(exam.title)}: results</h1>
      ${attempt.timedOut ? `<p class="notice">Time ran out, so the exam ended automatically.</p>` : ""}
      <div class="score-card">
        <div class="score">${score}<span>/${max}</span></div>
        <div class="score-meta">
          <div>Time used: <strong>${formatClock(used)}</strong> of ${exam.durationMin}:00</div>
          <div class="muted small">Marks are split evenly across each question's tests (best submission).</div>
        </div>
      </div>
      <table class="results-table">
        <thead><tr><th>#</th><th>Question</th><th>Tests passed</th><th class="num-cell">Marks</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <h2 class="section-title">Review your answers</h2>
      ${reviews}
      <div class="start-row">
        <button class="btn" type="button" data-act="retake">Retake this exam</button>
        <a class="btn btn-ghost" href="#/exams">Back to mock exams</a>
      </div>
    </div>`;
  highlightCode(app);
  app.querySelector('[data-act="retake"]').addEventListener("click", () => {
    if (!confirm("Start again? This clears your answers and score for this exam.")) return;
    clearAttempt(exam.id);
    route();
  });
}

boot();
