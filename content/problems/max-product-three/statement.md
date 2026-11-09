Write `maximum_product(nums)` that returns the largest product of any **three** numbers in `nums`.

> [!PROF-NOTE] Week 9 seminar slides, exercise 5
>
> The seminar's array had only **positive** numbers, so sorting and multiplying the last three was enough. Here numbers can be negative: the two smallest (most negative) times the largest can win, as in `[-10, -10, 1, 3]` → 300, not 30.

### Examples

```text
maximum_product([1, 2, 3])          →  6
maximum_product([1, 2, 3, 4])       →  24
maximum_product([-10, -10, 1, 3])   →  300
```

### Constraints

- `3 <= len(nums) <= 10 000`; `-1000 <= nums[i] <= 1000`
