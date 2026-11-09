## How it works (lecture)

Grow a sorted part on the left, one value at a time:

1. **Remove** the next value into a temporary variable (`temp`), leaving a gap.
2. **Compare** `temp` with each value on the left of the gap. While that value is **bigger**, **shift** it one place right (the gap moves left).
3. Stop at a value ≤ `temp`, or at the start, and **insert** `temp` into the gap.

```python
def insertion_sort(arr):
    comparisons = shifts = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = i - 1
        while pos >= 0:
            comparisons += 1
            if arr[pos] > temp:
                arr[pos + 1] = arr[pos]      # shift right
                shifts += 1
                pos -= 1
            else:
                break
        arr[pos + 1] = temp                  # insert into the gap
    return comparisons, shifts
```

## Counting the steps (lecture)

There are four kinds of step: removals, comparisons, shifts and insertions.

| Case | Comparisons | Shifts | Total |
|---|---|---|---|
| **Worst** (reverse order) | N(N − 1)/2 | N(N − 1)/2 | N² + N − 2 → **O(N²)** |
| **Best** (already sorted) | N − 1 | 0 | about 2(N − 1) → **O(N)** |
| Average | | | ≈ N²/2 |

The number of shifts equals the number of **inversions** (pairs in the wrong order). So insertion sort is **fast on nearly sorted data**, which makes it the best of the simple sorts in practice.

## Selection or insertion?

- Worst case: selection sort is a little faster (N²/2 compared with N²).
- Average and nearly sorted: **insertion sort** wins, and it's also **stable**.

## Binary insertion sort (Week 7, exercise 4)

The left part is sorted, so you can find where `temp` belongs with **binary search**: O(log N) comparisons instead of O(N). The **shifts** are still O(N) per insert, so the whole sort is still O(N²), but with fewer comparisons.

## Online

Insertion sort handles values **as they arrive**: each new value is inserted into an already sorted list. That makes it a natural fit for keeping a running median of a stream, or for sorting a **linked list** (where inserting is cheap once you've found the spot).
