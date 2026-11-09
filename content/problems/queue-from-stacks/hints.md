Push onto an **in** stack. For `pop` and `peek`, use an **out** stack.

---

When **out** is empty, first move everything from **in** to **out**, which reverses the order. Each value is moved once, so every operation is O(1) on average.
