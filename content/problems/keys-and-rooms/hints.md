This is reachability from room 0 in a directed graph: room `i` has an edge to each room it holds a key for. Use DFS or BFS with a `visited` set, then check whether every room was visited.

---

Up to 1 000 rooms can form a long chain (0 → 1 → 2 → …), which is too deep for recursive DFS in Python. Use a stack or a queue.
