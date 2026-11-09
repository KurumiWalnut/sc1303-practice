`intervals[i] = [left, right]` covers every whole number from `left` to `right`, **inclusive**. Put the intervals into groups so no two intervals in the same group share a number. Write `min_groups(intervals)` that returns the fewest groups needed.

### Examples

```text
min_groups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])   →  3
min_groups([[1, 3], [5, 6], [8, 10], [11, 13]])          →  1
```

### Constraints

- Up to 100 000 intervals; `1 <= left <= right <= 10⁶`.
