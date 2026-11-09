## How it works

Each pass-through **selects** the smallest value in the unsorted part and swaps it into the first unsorted position.

```text
[4, 2, 7, 1, 3]
pass 1: smallest is 1 → swap with index 0 → [1, 2, 7, 4, 3]
pass 2: smallest of [2, 7, 4, 3] is 2, already in place → no swap
pass 3: smallest of [7, 4, 3] is 3 → swap → [1, 2, 3, 4, 7]
pass 4: smallest of [4, 7] is 4, already in place → no swap
```

```python
def selection_sort(arr):
    comparisons = swaps = 0
    for i in range(len(arr) - 1):
        lowest = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[lowest]:
                lowest = j
        if lowest != i:                  # swap only if needed
            arr[i], arr[lowest] = arr[lowest], arr[i]
            swaps += 1
    return comparisons, swaps
```

## Counting the steps (lecture)

- comparisons = (N − 1) + (N − 2) + … + 1 = **N(N − 1)/2**, **always**, even on sorted input
- swaps: at most **one per pass**, so at most N − 1
- total ≈ N²/2 → **O(N²)**

Selection sort makes about half the steps of bubble sort in the worst case. Both are still O(N²). Unlike bubble and insertion sort, selection sort can't stop early on sorted data.

## Stopping early: the k-th smallest (Week 7, exercise 3)

After `k` passes, the first `k` positions hold the `k` smallest values in order. So the k-th smallest only needs **k passes**: about k × N comparisons, which is O(N) when k is small.

## Few swaps: the cycle trick

Selection sort makes at most N − 1 swaps. On a **permutation** of 0 … N − 1, the smallest possible number of swaps (of any two elements) is **N − (number of cycles)**. Follow each value to the index where it belongs: each cycle of length L takes L − 1 swaps to fix.

## Not stable

A long-distance swap can jump a value over an equal one. So selection sort isn't **stable**.
