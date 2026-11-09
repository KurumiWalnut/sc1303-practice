Trying every pair is O(N²). Instead, walk through once with a dict from value to index.

---

For each `x`, check whether `target - x` is already in the dict **before** adding `x`.
