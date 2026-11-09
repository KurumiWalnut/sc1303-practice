`nums` is sorted in ascending order and may contain repeats. Write `search_range(nums, target)` that returns `[first, last]`: the first and last index of `target`, or `[-1, -1]` if it isn't there. It must be O(log N).

### Examples

```text
search_range([5, 7, 7, 8, 8, 10], 8)   →  [3, 4]
search_range([5, 7, 7, 8, 8, 10], 6)   →  [-1, -1]
search_range([], 0)                    →  [-1, -1]
```

### Constraints

- Up to 500 000 values; the big test asks 20 000 questions.
