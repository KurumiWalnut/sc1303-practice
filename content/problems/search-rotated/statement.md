A sorted list of **distinct** numbers has been rotated at some unknown point, e.g. `[0, 1, 2, 4, 5, 6, 7]` became `[4, 5, 6, 7, 0, 1, 2]`. Write `search(nums, target)` that returns the index of `target`, or `-1`. It must be O(log N).

### Examples

```text
search([4, 5, 6, 7, 0, 1, 2], 0)   →  4
search([4, 5, 6, 7, 0, 1, 2], 3)   →  -1
search([1], 0)                     →  -1
```

### Constraints

- Up to 500 000 values; the big test asks 20 000 questions.
