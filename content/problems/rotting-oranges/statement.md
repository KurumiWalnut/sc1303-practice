In the grid, `0` is an empty cell, `1` is a fresh orange and `2` is a rotten one. Every minute, each fresh orange **next to** (up, down, left or right) a rotten one becomes rotten. Write `oranges_rotting(grid)` that returns the number of minutes until no fresh orange is left, or `-1` if some can never rot.

### Examples

```text
oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])   →  4
oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])   →  -1   (the bottom-left orange is cut off)
oranges_rotting([[0, 2]])                            →  0    (nothing fresh to begin with)
```

### Constraints

- Up to 200 × 200 cells.
