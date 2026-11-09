Counting every pair is O(N²), too slow for 50 000 values. Use **merge sort**, and count while merging.

---

When you take a value from the **right** half before the left half is used up, it jumps ahead of every value still waiting in the left half. Add that many inversions. O(N log N).
