`perm` holds each of the numbers `0` to `n - 1` exactly once. In one swap you can exchange **any two** positions. Write `minimum_swaps(perm)` that returns the fewest swaps needed to sort it.

### Examples

```text
minimum_swaps([1, 0, 3, 2])      →  2      cycles (0 1) and (2 3)
minimum_swaps([2, 0, 1])         →  2      one cycle of length 3
minimum_swaps([0, 1, 2])         →  0
```

### Constraints

- Up to 100 000 values.
