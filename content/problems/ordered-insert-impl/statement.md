`arr` is sorted in ascending order. Write:

- **`ordered_insert(arr, value)`**: insert `value` in place, keeping `arr` sorted, the way the lecture counts it, and return the number of **steps**:
  1. Compare from the left until you find the first value **bigger than** `value` (1 step per comparison; if none is bigger, that's N comparisons).
  2. Shift every value from there one place right (1 step per shift).
  3. Put `value` in the gap (1 step).
- **`ordered_search(arr, target)`**: linear search that **stops early** once it sees a value bigger than `target`. Return `(index, steps)` or `(-1, steps)`, where steps = comparisons made.

Don't use `list.insert`, `bisect` or `index`.

### Examples (lecture)

```text
a = [6, 28, 82, 120, 230]
ordered_insert(a, 65)   →  7       (3 comparisons + 3 shifts + 1 insert = N + 2)
a                       →  [6, 28, 65, 82, 120, 230]

ordered_search([6, 28, 82, 120, 230], 82)   →  (2, 3)
ordered_search([6, 28, 82, 120, 230], 65)   →  (-1, 3)     (82 > 65: stop)
```
