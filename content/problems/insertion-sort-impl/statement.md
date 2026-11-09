Write `insertion_sort(arr)` that sorts `arr` **in place** and returns `(comparisons, shifts)`, following the lecture:

1. For each index `i` from 1, take `arr[i]` out into `temp`.
2. Compare `temp` with the values on its left, starting next to it. While the value is **bigger** than `temp`, shift it one place right (1 comparison + 1 shift).
3. Stop at the first value that **isn't** bigger (that's 1 more comparison), or at the start of the list (no extra comparison). Put `temp` in the gap.

### Examples (lecture)

```text
a = [5, 4, 3, 2, 1];  insertion_sort(a)   →  (10, 10)   worst case
a = [1, 2, 3, 4, 5];  insertion_sort(a)   →  (4, 0)     best case: one comparison per value
a = list("DCAEB");    insertion_sort(a)   →  a is ['A', 'B', 'C', 'D', 'E']
```
