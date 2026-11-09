There are `n` cities, `0` to `n - 1`. `flights[i] = [from, to, price]` is a one-way flight. Write `find_cheapest_price(n, flights, src, dst, k)` that returns the cheapest price from `src` to `dst` using **at most `k` stops** (so at most `k + 1` flights), or `-1` if there's no such route.

### Examples

```text
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
find_cheapest_price(4, flights, 0, 3, 1)   →  700     (0 → 1 → 3; 0 → 1 → 2 → 3 needs 2 stops)

flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
find_cheapest_price(3, flights, 0, 2, 1)   →  200
find_cheapest_price(3, flights, 0, 2, 0)   →  500
```

### Constraints

- `1 <= n <= 100`; up to `n * (n - 1) / 2` flights; `0 <= k < n`.
