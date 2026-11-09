Trying `k = 1, 2, 3, …` is far too slow when piles hold a billion bananas.

---

At speed `k`, pile `p` takes `ceil(p / k)` hours, which is `(p + k - 1) // k`. Faster never takes longer, so binary search on `k` between `1` and `max(piles)`: if speed `mid` finishes in time, try slower (`high = mid`); otherwise try faster (`low = mid + 1`).
