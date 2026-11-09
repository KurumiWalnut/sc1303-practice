`cost[i]` is what you pay to step **off** step `i`; after paying, you climb 1 or 2 steps. You can start on step 0 or step 1 for free. Write `min_cost_climbing_stairs(cost)` that returns the cheapest total cost to reach the **top**, just past the last step.

> [!PROF-BUG] Week 9 seminar notebook, minCostClimbingStairs
>
> The notebook version starts at the top, `i = len(cost)`, and works out `cost[i] + min(...)`. There's no `cost[len(cost)]`, so it always crashes with an `IndexError`. Its base case is off too: it returns `0` for steps 0 and 1, so their costs are never paid, and even with the crash fixed `[10, 15, 20]` gives 0 instead of 15.
>
> The version on the slides is correct: `f(i) = cost[i] + min(f(i - 1), f(i - 2))`, with `f(0) = cost[0]` and `f(1) = cost[1]`, and the answer is `min(f(n - 1), f(n - 2))`.

### Examples

```text
min_cost_climbing_stairs([10, 15, 20])                          →  15
min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])  →  6
```

### Constraints

- `2 <= len(cost) <= 800`; `0 <= cost[i] <= 999`
