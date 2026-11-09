There are `n` cities, numbered `0` to `n - 1`, and `roads[i] = [a, b]` is a two-way road between `a` and `b`. The **network rank** of two different cities is the number of roads touching **either** of them. A road joining the two is counted **once**, not twice.

Write `maximal_network_rank(n, roads)` that returns the largest network rank over every pair of cities.

### Examples

```text
maximal_network_rank(4, [[0, 1], [0, 3], [1, 2], [1, 3]])                  →  4
maximal_network_rank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]])  →  5
maximal_network_rank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]])  →  5
```

### Constraints

- `2 <= n <= 100`; each pair of cities has at most one road.
