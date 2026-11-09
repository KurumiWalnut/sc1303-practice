## An array that stays sorted

An **ordered array** keeps its values in order at all times. Every insert has to put the new value in the **right place**, not just at the end.

## Inserting: search, shift, insert (lecture)

To insert 65 into `[6, 28, 82, 120, 230]`:

1. **Compare** from the left until you find the first value bigger than 65: compare with 6, 28 and 82. That's **3** comparisons.
2. **Shift** everything from there one place right: 230, 120 and 82. That's **3** shifts.
3. **Insert** 65 into the gap: **1** step.

That's 7 steps in total, which is **N + 2** for N = 5. It's roughly N + 2 wherever the value goes: fewer comparisons mean more shifts, and the other way round. If the value goes at the very end, there's nothing to shift: N comparisons + 1 insert = **N + 1**.

```python
def ordered_insert(arr, value):
    steps, i = 0, 0
    while i < len(arr):
        steps += 1                      # compare
        if arr[i] > value:
            break
        i += 1
    arr.append(None)
    for j in range(len(arr) - 1, i, -1):
        arr[j] = arr[j - 1]             # shift right
        steps += 1
    arr[i] = value
    return steps + 1                    # + the insert itself
```

## Searching gets faster

- **Linear search can stop early:** once you pass a value bigger than the target, the target can't be further on.
- **Binary search** works now: O(log N) instead of O(N).

That's the trade-off: **slower inserts, much faster searches**. It's worth it when you search far more often than you insert.

## Two-pointer merges

Two sorted arrays can be merged in **one pass**: compare the fronts and take the smaller. Filling from the **back** avoids overwriting when you merge into an array that has spare room at the end (*Merge Sorted Array*).

A sorted array squared isn't sorted (negatives!), but the biggest square is at **one of the two ends**. Fill the answer from the back, taking the larger end each time (*Squares of a Sorted Array*).

## 3Sum: sort + two pointers

Sort, then fix the first number `a`. Look for two numbers summing to `-a` in the rest with two pointers moving inwards. That's O(N²) instead of O(N³). Skip repeated values so each triplet is reported once.
