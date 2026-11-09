Calling `min()` on the whole stack is O(N).

---

Instead, store the **minimum so far** alongside each value when you push, for example as pairs `(val, min_so_far)`. Popping then brings back the previous minimum by itself.
