# SC1303 Practice

A study site for SC1303 weeks 5–12. It has a topic tree (part → topic → subtopic), and each subtopic has notes, a base implementation question and LeetCode-style problems. A Python judge runs in the browser, and there's a tab of timed mock exams in the final quiz format (4 questions, 90 minutes).

It currently has all 30 subtopics written, with 137 problems (base implementations plus LeetCode-style practice, roughly Easy → Medium → Hard in each subtopic), and 2 mock exams of 4 questions each.

It's a static site with no server, database or build step. Python runs in each visitor's browser through [Pyodide](https://pyodide.org).

## Run it locally

```bash
cd platform
python3 -m http.server 8000
```

Open http://localhost:8000. Opening `index.html` directly from your files won't work, because the browser blocks loading the content files that way.


## How it's organised

```text
index.html, css/, js/        the site itself
judge/harness.py             runs one test case (used by the browser AND by tools/verify.py)
content/
  tree.json                  parts → topics → subtopics ("leaves")
  exams.json                 mock exams
  notes/<leaf>.md            notes for each ready subtopic
  problems/<id>/
    problem.json             title, difficulty, tests
    statement.md             the question (what to do, not how to do it)
    hints.md                 optional hints, shown one at a time in the Hints tab
    starter.py               code students start from
    solution.py              reference solution (shown after trying, or after a mock)
    provided.py              optional code loaded before the student's (e.g. a Vertex class)
tools/verify.py              checks every problem before you publish
```

### Subtopics

A subtopic in `tree.json` is either:

- **ready**: `"status": "ready"`, with `notes`, `base` (a problem id, a list of ids such as `["lomuto-impl", "hoare-impl"]`, or `null`) and `practice` (a list of problem ids), or
- **planned**: `"status": "planned"`, with an `outline`, and placeholder entries in `base` and `practice`, e.g. `{ "title": "Two Sum", "lc": 1, "slug": "two-sum", "difficulty": "Easy" }`. Planned subtopics show as labelled wireframes.

To finish a planned subtopic, write its notes and problems, then switch it to `ready`.

### Hints

Keep the approach out of `statement.md`. Put it in `hints.md` instead, from a gentle nudge to the full method, with a line of `---` between hints:

```markdown
Trying every pair is O(N²). A dict can help.

---

For each `x`, check whether `target - x` is already in the dict **before** adding `x`.
```

Then set `"hints"` in `problem.json` to the number of hints (here `2`). Mock exams never show hints.

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
- `hidden` tests only run on **Submit**. Their input isn't shown.
- A problem can set `checker` (Python code defining `check(actual, expected)`) when more than one answer is right, e.g. groups in any order.
- Add at least one large hidden test so slow solutions time out, and check that they really do.

- **The test cases are public.** The judge runs in the browser, so anyone can read the tests (and solutions) in the site's files. That's fine for a study tool, but don't use it for anything graded.
- **First run downloads about 10 MB** (Python for the browser). After that it's cached.
- **Progress is saved in each browser only** (localStorage). Accounts and leaderboards would need a server.
- Problem statements are written for this site. LeetCode links point to the original problems.
