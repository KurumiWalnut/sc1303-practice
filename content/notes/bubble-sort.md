## How it works

Go through the array comparing **neighbours**, and swap any pair that's out of order. After the first **pass-through**, the largest value has "bubbled" to the end. Repeat on the rest.

```text
[4, 2, 7, 1, 3]
pass 1: 4>2 swap → [2, 4, 7, 1, 3]; 4<7 ok; 7>1 swap → [2, 4, 1, 7, 3]; 7>3 swap → [2, 4, 1, 3, 7]
pass 2: ... → [2, 1, 3, 4, 7]
pass 3: ... → [1, 2, 3, 4, 7]
pass 4: no swaps → done
```

## Two easy improvements

1. **Shrink the range:** after each pass, the last value of the unsorted part is in its final place, so the next pass can stop one sooner.
2. **Stop early** (Week 7, exercise 1): if a whole pass makes **no swaps**, the array is sorted. On already-sorted input, that's one pass of N − 1 comparisons: **O(N)**.

```python
def bubble_sort(arr):
    comparisons = swaps = 0
    unsorted_until = len(arr) - 1          # the last index of the unsorted part
    swapped = True
    while swapped and unsorted_until > 0:
        swapped = False
        for i in range(unsorted_until):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        unsorted_until -= 1
    return comparisons, swaps
```

A further trick (exercise 2): remember **where** the last swap happened. Everything after it is already sorted, so the next pass only has to go up to there.

## Counting the steps (lecture)

For N values in reverse order:

- comparisons = (N − 1) + (N − 2) + … + 1 = **N(N − 1)/2**
- swaps: every comparison swaps, so also **N(N − 1)/2**
- total ≈ **N² − N** → **O(N²)**

## Swaps = inversions

Each swap fixes exactly **one** pair that's in the wrong order (an **inversion**). So bubble sort's swap count = the number of inversions = the **minimum number of adjacent swaps** needed to sort. Counting inversions quickly (in O(N log N)) is a classic merge-sort trick: when you take a value from the **right** half during a merge, it jumps ahead of every value still waiting in the left half.

## Stable

Bubble sort only swaps when `arr[i] > arr[i + 1]` (strictly), so equal values keep their order. A sort with this property is **stable**.
