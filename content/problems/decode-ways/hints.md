Let `ways(i)` = the number of ways to decode `s[i:]`. At position `i`:

- if `s[i]` isn't `"0"`, take **one** digit: add `ways(i + 1)`;
- if `s[i:i+2]` is between `"10"` and `"26"`, take **two** digits: add `ways(i + 2)`.

---

`ways(len(s)) = 1` (nothing left to decode). Without a memo, the two branches double the work at every step.
