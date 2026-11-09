Draw an edge `b → a` for each pair. You can finish everything exactly when this directed graph has **no cycle**.

---

Use **Kahn's algorithm**: count each course's in-degree (how many prerequisites it has), start a queue with every course that has none, and "take" courses from the queue, lowering the in-degree of the courses that depend on them. If you take all `num_courses`, the answer is `True`.

A chain of 2 000 prerequisites is too deep for recursive DFS in Python, so the queue version is the safe choice.
