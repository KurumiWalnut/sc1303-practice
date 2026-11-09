## The idea

Binary search finds a value in a **sorted** array. It checks the middle cell, then throws away the half that can't contain the target, and repeats.

| Array size | Linear search (worst case) | Binary search (worst case) |
|---|---|---|
| 9 | 9 steps | 4 steps |
| 100 000 | 100 000 steps | 17 steps |
| about 1 million (2²⁰) | about 1 million steps | about 20 steps |

Doubling the array adds **one** step to binary search, but doubles the steps of a linear search.

## Why it's O(log N)

After each step, half of the cells are left: N → N/2 → N/4 → … → N/2ˣ. The search ends when one cell is left:

N / 2ˣ = 1  →  N = 2ˣ  →  x = log₂ N

## Template

```python
def binary_search(array, target):
    low, high = 0, len(array) - 1      # target can only be in array[low..high]
    while low <= high:                 # the range isn't empty yet
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            low = mid + 1              # throw away the left half (and mid)
        else:
            high = mid - 1             # throw away the right half (and mid)
    return -1                          # the range is empty: not found
```

If the loop ends without finding the target, `low` is where the target **would be inserted** to keep the array sorted. That one fact solves *Search insert position*.

## Ordered arrays: the trade-off

Keeping an array sorted makes **insertion slower**: you search for the right spot and shift everything after it, about N + 2 steps. In return, **searching** drops from O(N) to O(log N).

## Binary search on the answer

You can binary search any range of possible answers where a yes/no check flips only once. For the integer square root of `n`, the answer is the largest `r` with `r * r ≤ n`, so binary search for `r` between `0` and `n`.

## Common bugs

- Writing `while low < high` with `high = mid - 1` skips the last candidate. Use `<=` with this template.
- Writing `low = mid` instead of `mid + 1` can loop forever when `low` and `high` are next to each other.
- Forgetting that the array must be sorted. Binary search on unsorted data gives wrong answers without any error.

> **Exam tip:** Python's `bisect` module does this for you, but implementation questions expect you to write the loop yourself.

## Three harder patterns

**First and last position.** To find the **first** index of `target`, don't stop when you see it: record the index and keep searching **left** (`high = mid - 1`). For the last index, keep searching right. Two binary searches give the whole range in O(log N).

**Rotated sorted array.** In `[4, 5, 6, 7, 0, 1, 2]`, cut anywhere and at least **one half is sorted**. Check which half is sorted (compare `array[low]` with `array[mid]`). If the target lies inside that sorted half's range, search there; otherwise search the other half.

**Binary search on the answer.** *Koko Eating Bananas* asks for the smallest eating speed that finishes in time. Faster always finishes sooner, so "can she finish at speed s?" flips from no to yes exactly once as `s` grows. Binary search on `s` between 1 and `max(piles)`, and check each guess in O(N): O(N log(max)) in total.
