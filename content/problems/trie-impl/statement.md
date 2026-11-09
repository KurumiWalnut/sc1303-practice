Build the course's trie. `TrieNode` is written for you: each node has a dict `children` mapping a character to the child node.

Write the `Trie` methods:

- **`insert(word)`**: add the word, creating nodes where the path is missing, then mark the end with `node.children["*"] = None`.
- **`search(word)`**: walk the characters from the root and return the **node** reached after the last one, or `None` if the path breaks.
- **`contains(word)`**: `True` only if `word` was inserted as a whole word.
- **`starts_with(prefix)`**: `True` if some inserted word starts with `prefix`.

Each method should take O(length of the word): don't loop over all the stored words.

### Example

```text
t = Trie()
for w in ["ace", "bad", "cat"]:
    t.insert(w)
t.contains("cat")             →  True
t.contains("ca")              →  False   (only a prefix)
t.starts_with("ca")           →  True
"*" in t.search("cat").children   →  True
sorted(t.root.children)       →  ['a', 'b', 'c']
```
