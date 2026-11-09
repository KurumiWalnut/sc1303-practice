You have a pile of stones with positive integer weights. Each turn, take the **two heaviest** stones, with weights `x ≤ y`, and smash them together:

- if `x == y`, both are destroyed;
- otherwise the `x` stone is destroyed and a stone of weight `y - x` goes back into the pile.

Repeat until at most one stone is left. Write `last_stone_weight(stones)` that returns the weight of the last stone, or `0` if none are left.

### Examples

```text
last_stone_weight([2, 7, 4, 1, 8, 1])  →  1
    smash 7 and 8 → 1 goes back:   [2, 4, 1, 1, 1]
    smash 2 and 4 → 2 goes back:   [2, 1, 1, 1]
    smash 1 and 2 → 1 goes back:   [1, 1, 1]
    smash 1 and 1 → both destroyed: [1]
last_stone_weight([2, 2])              →  0
```

### Constraints

- `1 ≤ len(stones) ≤ 5 000`, `1 ≤ stones[i] ≤ 1 000`
