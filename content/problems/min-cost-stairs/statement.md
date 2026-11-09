`cost[i]` is what you pay to step **off** step `i`; after paying, you climb 1 or 2 steps. You can start on step 0 or step 1 for free. Write `min_cost_climbing_stairs(cost)` that returns the cheapest total cost to reach the **top**, just past the last step.

### Examples

```text
min_cost_climbing_stairs([10, 15, 20])                          →  15
min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])  →  6
```

### Constraints

- `2 <= len(cost) <= 800`; `0 <= cost[i] <= 999`
