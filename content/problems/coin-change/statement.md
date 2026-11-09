Write `coin_change(coins, amount)` that returns the **fewest** coins that add up to `amount`, or `-1` if it can't be done. You have as many of each coin as you like.

### Examples

```text
coin_change([1, 2, 5], 11)   →  3      (5 + 5 + 1)
coin_change([2], 3)          →  -1
coin_change([1], 0)          →  0
```

### Constraints

- `1 <= len(coins) <= 12`; `0 <= amount <= 10 000`
