Write `kth_largest(nums, k)` that returns the **k-th largest** value in `nums`.

It's the k-th largest in sorted order, not the k-th distinct value: in `[3, 2, 3, 1, 2, 4, 5, 5, 6]` the 4th largest is `4` (6, 5, 5, **4**).

### Examples

```text
kth_largest([3, 2, 1, 5, 6, 4], 2)           →  5
kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)  →  4
```

### Constraints

- `1 ≤ k ≤ len(nums) ≤ 100 000`
- `-10⁴ ≤ nums[i] ≤ 10⁴`
