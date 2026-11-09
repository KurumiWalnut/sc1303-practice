A loop is O(N), far too slow when `n` is 10¹⁸. Find a **formula**.

---

With `m = n // 2` even numbers,

```text
2 + 4 + … + 2m = 2 × (1 + 2 + … + m)
```

and `1 + 2 + … + m = m (m + 1) / 2`. Use integer arithmetic (`//`) so big answers stay exact.
