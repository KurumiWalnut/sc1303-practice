Write `pivot_array(nums, pivot)` that returns a new list with:

1. every value **less than** `pivot` first,
2. then every value **equal to** `pivot`,
3. then every value **greater than** `pivot`,

and the values inside each group kept in their **original order** (a *stable* partition).

### Examples

```text
pivot_array([9, 12, 5, 10, 14, 3, 10], 10)   →  [9, 5, 3, 10, 10, 12, 14]
pivot_array([-3, 4, 3, 2], 2)                →  [-3, 2, 4, 3]
```
