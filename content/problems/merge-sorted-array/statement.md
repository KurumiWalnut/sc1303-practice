`nums1` has length `m + n`: its first `m` values are sorted, and the last `n` slots are 0s you can overwrite. `nums2` holds `n` sorted values. Write `merge(nums1, m, nums2, n)` that merges `nums2` into `nums1` **in place**, so `nums1` ends up sorted. Return nothing.

### Examples

```text
nums1 = [1, 2, 3, 0, 0, 0];  merge(nums1, 3, [2, 5, 6], 3)   →  nums1 is [1, 2, 2, 3, 5, 6]
nums1 = [1];                 merge(nums1, 1, [], 0)          →  [1]
nums1 = [0];                 merge(nums1, 0, [1], 1)         →  [1]
```
