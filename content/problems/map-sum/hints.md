Looping over every key in `sum` is too slow for the big tests.

---

Instead, keep a running **total** on every trie node for the keys that pass through it. When a key's value changes, add the **difference** to each node on its path. `sum` is then a walk down the prefix.
