Start with a positive whole number. Replace it with the **sum of the squares of its digits**, and keep going. If you reach `1`, the number is **happy**. Otherwise the numbers go round a loop forever.

Write `is_happy(n)` that returns `True` if `n` is happy and `False` if it loops forever.

### Examples

```text
is_happy(19)   →  True     19 → 82 → 68 → 100 → 1
is_happy(2)    →  False    2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...
```

### Constraints

- `1 <= n <= 2³¹ - 1`
