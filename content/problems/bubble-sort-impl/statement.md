Write `bubble_sort(arr)` that sorts `arr` **in place** and returns `(comparisons, swaps)`.

- A **pass-through** compares each pair of neighbours across the unsorted part, swapping them when the left one is **bigger** (equal values aren't swapped).
- After each pass, the last value of the unsorted part is in its final place, so the **next pass stops one position earlier**.
- **Stop** after a pass that makes **no swaps**, or when the unsorted part is down to one value.

Count 1 comparison each time you compare two neighbours, and 1 swap each time you swap them.

### Examples (lecture)

```text
a = [5, 4, 3, 2, 1];  bubble_sort(a)   →  (10, 10)    4 + 3 + 2 + 1 comparisons, all of them swap
a = [1, 2, 3, 4, 5];  bubble_sort(a)   →  (4, 0)      one pass, no swaps: stop
a = [4, 2, 7, 1, 3];  bubble_sort(a)   →  a is [1, 2, 3, 4, 7]
```
