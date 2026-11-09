Write `binary_search(array, target)`.

`array` is a list of **distinct** integers sorted in ascending order. Return the index of `target` in `array`, or `-1` if it isn't there.

Your search must take **O(log N)** steps: look at the middle element, then throw away the half that can't contain `target`. Don't use `in`, `.index()` or the `bisect` module.

> [!PROF-NOTE] Week 6 seminar notebook
>
> The seminar's `binary_search` also counts its steps and returns `(index, steps)`, or `("Not found", steps)`. Here, return just the index, or `-1`. In the quiz, return whatever the question asks for.

### Examples

```text
binary_search([2, 4, 6, 8, 10, 12, 14, 16, 18], 14)  →  6
binary_search([3, 17, 75, 80, 202], 22)              →  -1
binary_search([5], 5)                                →  0
```

### Constraints

- `0 ≤ len(array) ≤ 500 000`
- The hidden tests search a large array thousands of times, so a linear scan will run out of time.
