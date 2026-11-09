`heights` is a grid of numbers. You start at the top-left cell and want to reach the bottom-right one, moving up, down, left or right. The **effort** of a route is the **largest** absolute height difference between two neighbouring cells along it. Write `minimum_effort_path(heights)` that returns the smallest possible effort.

### Examples

```text
minimum_effort_path([[1, 2, 2], [3, 8, 2], [5, 3, 5]])                  →  2
minimum_effort_path([[1, 2, 3], [3, 8, 4], [5, 3, 5]])                  →  1
minimum_effort_path([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]])  →  0
```

### Constraints

- Up to 100 × 100 cells; heights between 1 and 1 000 000.
