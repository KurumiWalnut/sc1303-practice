Moving everything one step `k` times is O(N·k). There's an O(N) way that only **reverses** parts of the list.

---

The O(N) way:

1. `k = k % len(nums)` (rotating by N changes nothing).
2. **Reverse** the whole list.
3. Reverse the first `k` values, then reverse the rest.

Each value is swapped about once: O(N) with no extra list. (`nums[:] = …` with slices also works and is O(N), but uses extra memory.)
