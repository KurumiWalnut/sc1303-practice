Aim for O(N) with a set.

---

1. Put every number in a set.
2. A number `x` **starts** a run only if `x - 1` isn't in the set.
3. From each start, count up while `x + 1`, `x + 2`, … are in the set.

Each number is counted in exactly one run, so the total work is O(N).
