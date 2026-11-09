A window of size `k` slides across `nums` from left to right, one step at a time. Write `max_sliding_window(nums, k)` that returns the **maximum** of each window.

### Examples

```text
max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)   →  [3, 3, 5, 5, 6, 7]
max_sliding_window([1], 1)                          →  [1]
```

### Constraints

- Up to 100 000 numbers; `1 <= k <= len(nums)`.
