`points` is a list of `[x, y]` points. Write `k_closest(points, k)` that returns the `k` points **closest to the origin** `(0, 0)`, in any order.

If two points tie for the last place, either one is fine.

### Examples

```text
k_closest([[1, 3], [-2, 2]], 1)              →  [[-2, 2]]
k_closest([[3, 3], [5, -1], [-2, 4]], 2)     →  [[3, 3], [-2, 4]]   (any order)
```

### Constraints

- `1 <= k <= len(points) <= 100 000`; coordinates are between -10 000 and 10 000.
