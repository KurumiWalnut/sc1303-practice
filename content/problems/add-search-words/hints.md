Store the words in a trie.

---

Ordinary letters walk down one child. A `.` has to try **every** child, so write `search` as a recursive DFS (or keep a list of the nodes you're currently on).
