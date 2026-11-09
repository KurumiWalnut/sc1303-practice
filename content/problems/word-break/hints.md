Let `can(i)` = "can `s[i:]` be split?". It's `True` if some word `w` in the dictionary matches `s` at position `i` **and** `can(i + len(w))`. `can(len(s))` is `True`.

---

Without a memo this tries the same `i` again and again, which is exponential on inputs like `"aaaa…ab"`.
