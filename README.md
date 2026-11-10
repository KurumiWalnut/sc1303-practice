# SC1303 Practice

Practise SC1303 data structures and algorithms (weeks 5–12) the way you'll be tested: short notes, coding problems checked by a Python judge in your browser, and timed mock exams.

**Open the site: https://kurumiwalnut.github.io/sc1303-practice/**

> An unofficial study tool made by SC1303 students. It isn't affiliated with the course team.

## What's inside

- **30 subtopics** in lecture order, each with short notes.
- **27 base implementations**: the core code from the course templates (heap, BST, AVL tree, Dijkstra and more) that you should be able to write from memory.
- **110 LeetCode-style problems** (44 Easy, 62 Medium, 4 Hard), from easy to hard within each subtopic. Most have hints you can open one at a time.
- **A Python judge in your browser.** Run the sample tests as often as you like, or submit to run the hidden tests too. No sign-up needed.
- **2 timed mock exams** in the final quiz format: 4 questions in 90 minutes, 25 marks each.
- **Exam prep:** a cheatsheet (which structure to pick, Big O, Python tools, the course templates, HackerEarth input and output) and every seminar coding exercise, linked to the problems that practise it.

## Topics

| Week | Topic | Subtopics |
|---|---|---|
| 5–6 | Arrays & Big O | Array operations, Big O notation |
| 6 | Searching | Ordered arrays, binary search |
| 7 | Simple sorts | Bubble, selection and insertion sort, sorting as a tool |
| 8 | Hash tables | Hashing & collisions, hash map patterns |
| 8 | Stacks & queues | Stacks, queues |
| 9–10 | Recursion & DP | Recursion & the call stack, memoization, DP problems |
| 10 | Quicksort | Partitioning (Lomuto and Hoare), quicksort & quickselect |
| 11 | Linked lists | Singly and doubly linked lists |
| 11 | Binary search trees | Search & insert, deletion, traversals |
| 11 | Tries | Insert & search, autocomplete |
| 12 | AVL trees | Balance factor, rotations |
| 12 | Heaps & priority queues | Max-heap |
| 12 | Graphs | Representations, DFS & BFS |
| 12 | Dijkstra's algorithm | Shortest paths |

## How to use it

1. Under **Learn**, pick a subtopic and read its notes.
2. Write the **base implementation**, then work through the **LeetCode-style** problems.
3. Press **Run samples** (⌘/Ctrl + Enter) to check the sample tests, and **Submit** (⌘/Ctrl + Shift + Enter) to run every test.
4. Stuck? Open the **Hints** tab one hint at a time. Each problem also has a reference solution behind a button.
5. When you're ready, sit a **mock exam**. It shows no notes or hints, and the timer keeps running even if you close the tab.

The code box has a full-screen button, and Esc exits full screen.

## Good to know

- **The first visit downloads about 10 MB** (Python for the browser). After that it's cached.
- **Your progress is saved in your browser only.** It doesn't sync between devices or browsers, and clearing your browsing data deletes it. To clear it yourself, use the **Reset my progress** link at the bottom of the home page.
- **Tests and solutions are public** in this repository, because the judge runs in your browser. That's fine for practice, but don't use the site for anything graded.
- Problem statements are written for this site. LeetCode links point to the original problems.

## Run it on your own computer

```bash
git clone https://github.com/KurumiWalnut/sc1303-practice.git
cd sc1303-practice
python3 -m http.server 8000
```

Then open http://localhost:8000. Opening `index.html` directly from your files won't work, because the browser blocks loading the content files that way.

It's a static site with no server, database or build step. Python runs in the browser through [Pyodide](https://pyodide.org), and the code editor is [CodeMirror](https://codemirror.net/5/).

## Adding or fixing problems

Everything a student sees comes from the `content/` folder:

```text
index.html, css/, js/        the site itself
logo.svg, apple-touch-icon.png   the sakura logo (header and browser tab; phone home screen)
judge/harness.py             runs one test case (used by the browser and by tools/verify.py)
content/
  tree.json                  parts → topics → subtopics ("leaves")
  exams.json                 mock exams
  prep/cheatsheet.md         the Exam prep cheatsheet
  prep/exercises.json        every seminar coding exercise, linked to the problems that practise it
  notes/<leaf>.md            notes for each subtopic
  icons/<topic>.svg          a picture for each topic (64×64 SVG)
  problems/<id>/
    problem.json             title, difficulty, tests
    statement.md             the question (what to do, not how to do it)
    hints.md                 optional hints, shown one at a time in the Hints tab
    starter.py               the code students start from
    solution.py              reference solution
    provided.py              optional code loaded before the student's (e.g. a Vertex class)
tools/verify.py              checks every problem
```

### Topics and subtopics

Each topic in `tree.json` can set `icon` (a path inside `content/`, e.g. `"icons/heaps.svg"`) and `tint` (the colour of the tile behind it, e.g. `"#e2eeff"`). The icons are original drawings made for this site.

A subtopic in `tree.json` is either:

- **ready**: `"status": "ready"`, with `notes`, `base` (a problem id, a list of ids such as `["lomuto-impl", "hoare-impl"]`, or `null`) and `practice` (a list of problem ids), or
- **planned**: `"status": "planned"`, with an `outline` and placeholder entries in `base` and `practice`, e.g. `{ "title": "Two Sum", "lc": 1, "slug": "two-sum", "difficulty": "Easy" }`. Planned subtopics show as labelled outlines.

### Hints

Keep the approach out of `statement.md`. Put it in `hints.md` instead, from a gentle nudge to the full method, with a line of `---` between hints:

```markdown
Trying every pair is O(N²). A dict can help.

---

For each `x`, check whether `target - x` is already in the dict **before** adding `x`.
```

Then set `"hints"` in `problem.json` to the number of hints (here `2`). Mock exams never show hints.

### Bugs and differences in the professor's code

When the professor's slides or notebooks have a bug, or do something differently from a problem here, flag it with a highlighted box in the notes or in `statement.md`. Write a quote whose first line is a marker, followed by where the code comes from:

```markdown
> [!PROF-BUG] Week 12 seminar solution, dijkstra.py
>
> What goes wrong, a small example, and the fix.
```

`[!PROF-BUG]` draws a red "Bug in the professor's code" box. `[!PROF-NOTE]` draws an amber "Differs from the professor's version" box.

### Tests

Each test in `problem.json` runs in a fresh Python namespace, in this order: provided code → student code → `data` → `setup` → `expr`.

```json
{
  "name": "Delete returns the max",
  "data": "values = [30, 20, 15]",
  "setup": "h = MaxHeap()\nfor v in values:\n    h.insert(v)",
  "expr": "(h.delete(), h.heap)",
  "expected": "(30, [20, 15])",
  "hidden": true,
  "hint": "Shown in practice mode when this hidden test fails.",
  "timeLimitMs": 5000
}
```

- `expected` is a Python expression. It's evaluated with only the provided code and `data` loaded, so student code can't change it.
- Building `data` doesn't count towards the time limit, so large inputs are fine.
- `hidden` tests only run on **Submit**, and their input isn't shown.
- A problem can set `checker` (Python code defining `check(actual, expected)`) when more than one answer is right, e.g. groups in any order.
- Add at least one large hidden test so slow solutions time out, and check that they really do.

### Check your changes

```bash
python3 tools/verify.py
```

This checks that every reference solution passes all its tests, that every starter fails at least one, and that `tree.json` and `exams.json` only point at problems that exist. To check only some problems, add their ids, e.g. `python3 tools/verify.py hoare-impl`.
