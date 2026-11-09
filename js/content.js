// Loads course content from the content/ folder (plain files, so classmates can add to it).
const cache = new Map();

function fetchFile(path, as = "text") {
  const key = `${as}:${path}`;
  if (!cache.has(key)) {
    const request = fetch(`content/${path}`, { cache: "no-cache" }).then((res) => {
      if (!res.ok) throw new Error(`Couldn't load content/${path} (${res.status})`);
      return as === "json" ? res.json() : res.text();
    });
    request.catch(() => cache.delete(key)); // allow a retry after a network blip
    cache.set(key, request);
  }
  return cache.get(key);
}

export const loadTree = () => fetchFile("tree.json", "json");
export const loadExams = () => fetchFile("exams.json", "json");
export const loadNotes = (path) => fetchFile(path);

export async function loadProblem(id) {
  const dir = `problems/${id}/`;
  const meta = await fetchFile(`${dir}problem.json`, "json");
  const [statement, starter, solution, prelude, hintsText] = await Promise.all([
    fetchFile(`${dir}statement.md`),
    fetchFile(`${dir}starter.py`),
    fetchFile(`${dir}solution.py`),
    meta.provided ? fetchFile(`${dir}provided.py`) : Promise.resolve(""),
    meta.hints ? fetchFile(`${dir}hints.md`) : Promise.resolve(""),
  ]);
  // hints.md holds one hint per section, separated by lines of `---`.
  const hints = hintsText.split(/\n---\n/).map((h) => h.trim()).filter(Boolean);
  return { ...meta, statement, starter, solution, prelude, hints };
}

export async function loadProblemMeta(id) {
  return fetchFile(`problems/${id}/problem.json`, "json");
}

/** A leaf's `base` as a list: it can be one entry, a list of entries, or null. */
export function baseList(leaf) {
  if (!leaf.base) return [];
  return Array.isArray(leaf.base) ? leaf.base : [leaf.base];
}

/** Problem ids attached to a leaf: the base implementations first, then practice problems. */
export function leafProblemIds(leaf) {
  return [...baseList(leaf), ...(leaf.practice || [])].filter((p) => typeof p === "string");
}

/** Flattens the tree so pages can look up a leaf, its topic and its part. */
export function indexTree(tree) {
  const leaves = new Map();
  const order = [];
  for (const part of tree.parts) {
    for (const topic of part.topics) {
      for (const leaf of topic.leaves) {
        leaves.set(leaf.id, { leaf, topic, part });
        order.push(leaf.id);
      }
    }
  }
  const ready = order.filter((id) => leaves.get(id).leaf.status === "ready");
  const readyProblems = ready.flatMap((id) => leafProblemIds(leaves.get(id).leaf));
  return { leaves, order, ready, readyProblems };
}
