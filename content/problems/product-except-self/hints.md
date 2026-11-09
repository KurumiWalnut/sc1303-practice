`answer[i]` = (product of everything **left** of `i`) × (product of everything **right** of `i`).

---

1. Pass left to right, filling `answer[i]` with the running product of the values before `i`.
2. Pass right to left with another running product, multiplying it into `answer[i]`.

Two passes: O(N). Multiplying everything else for each `i` is O(N²).
