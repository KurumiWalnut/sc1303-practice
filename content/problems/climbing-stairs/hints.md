Your last move to step `n` came either from step `n - 1` or from step `n - 2`.

---

So `ways(n) = ways(n - 1) + ways(n - 2)`. Find the base cases, then loop. You only need the last two values.
