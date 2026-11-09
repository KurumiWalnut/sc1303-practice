The region is connected, so every row from its top row to its bottom row has at least one black pixel, and no row outside that range has any. The same goes for columns.

---

Ask "does row `r` have a black pixel?" for rows `0` to `x`: the answer is No, No, …, No, Yes, Yes, …, Yes (row `x` is a Yes). Binary search for the first Yes: that's the top. Do the same for rows `x` to the end (the last Yes is the bottom), and for columns. Each question costs one row or column scan, so the total is O(m log n + n log m) instead of O(m × n).
