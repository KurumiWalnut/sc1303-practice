Bubbling each zero to the end works but is O(N²).

---

In one pass: keep a **write** index for the next non-zero value. Swap each non-zero value you meet into `nums[write]`, then move `write` on. The zeros end up behind.
