Trying every start and end is O(N²). **Kadane's algorithm** does it in one pass.

---

Keep `best_here`, the best sum of a subarray **ending at the current position**:

```text
best_here = max(x, best_here + x)     # extend the run, or start again at x
best      = max(best, best_here)
```
