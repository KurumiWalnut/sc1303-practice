`intervals` is a list of `[start, end]` pairs. Write `merge_intervals(intervals)` that merges every group of overlapping intervals and returns the result **sorted by start**. Intervals that only touch (`[1, 4]` and `[4, 5]`) count as overlapping.

### Examples

```text
merge_intervals([[2, 6], [15, 18], [8, 10], [1, 3]])   →  [[1, 6], [8, 10], [15, 18]]
merge_intervals([[1, 4], [4, 5]])                      →  [[1, 5]]
```

### Constraints

- Up to 100 000 intervals.
