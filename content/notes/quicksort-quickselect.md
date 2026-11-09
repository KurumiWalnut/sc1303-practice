## Quicksort

1. **Partition** the subarray: the pivot lands in its final place, at index `p`.
2. Quicksort the part **left** of `p`.
3. Quicksort the part **right** of `p`.

The base case is a subarray with 0 or 1 elements (`low >= high`), which is already sorted.

```python
def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        p = partition(array, low, high)      # Lomuto, pivot = last element
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)
```

It sorts **in place**: nothing is returned, and the list you passed in is changed.

## How fast?

| Case | When | Time |
|---|---|---|
| Best / average | pivots split the array roughly in half | **O(N log N)** |
| Worst | pivot is always the smallest or largest, e.g. **already sorted** input with a last-element pivot | **O(N²)** |

Compare insertion sort: O(N) best case, O(N²) average and worst. Quicksort wins on average, which is why it's so widely used.

### Fixing the worst case

- **Random pivot:** swap a random element into `high` before partitioning. Sorted input is then no worse than any other.
- **Many equal values:** Lomuto puts all the equal values on one side, so an all-equal array is O(N²) too. A **three-way** partition (less / equal / greater) fixes this.
- In Python, a worst-case quicksort also recurses N levels deep and hits the **recursion limit** (about 1000).

## Quickselect: the k-th smallest without sorting

After one partition, the pivot is at index `p`, its sorted position. If you want the value at sorted index `k`:

- `k == p`: it's the pivot. Done.
- `k < p`: it's in the **left** part, so recurse there only.
- `k > p`: it's in the **right** part, so recurse there only.

```python
def quickselect(array, k, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low == high:
        return array[low]
    p = partition(array, low, high)
    if k == p:
        return array[p]
    if k < p:
        return quickselect(array, k, low, p - 1)
    return quickselect(array, k, p + 1, high)
```

Each step throws away one side, so the average work is N + N/2 + N/4 + … ≈ 2N: **O(N)**. The worst case is still O(N²).

## Where it's used

- **Median**: `quickselect(array, len(array) // 2)` for an odd length.
- **Top k / k closest**: quickselect around index `k`. The first `k` positions then hold the answer, in some order.

## Common bugs

- Recursing on `(low, p)` instead of `(low, p - 1)`, which never shrinks.
- Comparing `k` with `p - low`: if `k` is an index in the **whole** array, compare it with `p` directly.
- Expecting `quick_sort` to return the list. It returns `None`; the list itself is sorted.
