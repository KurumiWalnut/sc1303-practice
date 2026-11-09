`grid` is a 2D list of strings: `"1"` is land and `"0"` is water. An **island** is a group of land cells connected **up, down, left or right** (not diagonally). Everything outside the grid is water.

Write `num_islands(grid)` that returns the number of islands.

You may change `grid`.

### Examples

```text
1 1 1 1 0
1 1 0 1 0        →  1
1 1 0 0 0
0 0 0 0 0

1 1 0 0 0
1 1 0 0 0        →  3
0 0 1 0 0
0 0 0 1 1
```

### Constraints

- `1 ≤ rows, columns ≤ 120`
