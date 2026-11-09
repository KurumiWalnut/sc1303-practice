Write `selection_sort(arr)` that sorts `arr` **in place** and returns `(comparisons, swaps)`.

For each position `i` from the start: scan the rest of the array for the **smallest** value (1 comparison each time you compare a value with the smallest found so far), then swap it into position `i`. **Don't swap** if the smallest is already at `i`.

### Examples (lecture)

```text
a = [4, 2, 7, 1, 3];  selection_sort(a)   →  (10, 2)    a is [1, 2, 3, 4, 7]
a = [1, 2, 3, 4, 5];  selection_sort(a)   →  (10, 0)    still N(N-1)/2 comparisons
```
