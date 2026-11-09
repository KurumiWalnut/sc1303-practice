Keep a running total `prefix`. A subarray ending at the current position sums to `k` exactly when some **earlier** running total was `prefix - k`.

---

So keep a dict counting how often each running total has appeared, starting with `{0: 1}` for the empty prefix.

Checking every start and end is O(N²), too slow for 20 000 numbers.
