Let `best[i]` be the cheapest way to stand on step `i`.

---

Then `best[0] = best[1] = 0` and

```text
best[i] = min(best[i - 1] + cost[i - 1], best[i - 2] + cost[i - 2])
```

and the answer is `best[len(cost)]`.
