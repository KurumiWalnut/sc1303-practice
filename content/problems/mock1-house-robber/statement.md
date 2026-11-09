A street has houses in a row, and `nums[i]` is the amount of money in house `i`. You can collect from any houses you like, **except two that are next to each other**.

Write `max_non_adjacent(nums)` that returns the most money you can collect.

### Examples

```text
max_non_adjacent([1, 2, 3, 1])     →  4     (houses 0 and 2: 1 + 3)
max_non_adjacent([2, 7, 9, 3, 1])  →  12    (houses 0, 2 and 4: 2 + 9 + 1)
max_non_adjacent([5])              →  5
max_non_adjacent([])               →  0
```

### Constraints

- `0 ≤ len(nums) ≤ 500`
- `0 ≤ nums[i] ≤ 400`
- Trying every combination is far too slow for 60 or more houses.
