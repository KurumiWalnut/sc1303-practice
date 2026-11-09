Write `count_inversions(nums)` that returns the **minimum number of swaps of neighbouring values** needed to sort `nums` in ascending order. This is exactly the number of **inversions**: pairs `i < j` with `nums[i] > nums[j]`. It's also the number of swaps bubble sort makes.

### Examples

```text
count_inversions([2, 4, 1, 3, 5])   →  3     (2,1), (4,1), (4,3)
count_inversions([1, 2, 3])         →  0
count_inversions([3, 2, 1])         →  3
```

### Constraints

- Up to 50 000 values; equal values are not an inversion.
