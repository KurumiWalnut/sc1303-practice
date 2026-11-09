Sorting works, but try a heap instead.

---

Keep a **min-heap of size k** holding the k largest values seen so far. Its root is the answer. That takes O(N log k).

> **Tip:** Python's `heapq` is a **min**-heap (`heappush`, `heappop`, `heapify`), unlike the course's max-heap.
