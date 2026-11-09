Write `quick_sort_trace(arr)` that sorts `arr` **in place** with the course's quicksort and returns a list of the **pivot indexes**, in the order `partition` returns them.

- Partition with **Lomuto**: pivot = `arr[high]`, pointer `b` starts at `low`, swap `arr[a]` into `arr[b]` when `arr[a] < pivot` (strictly), then swap the pivot into `arr[b]` and return `b`.
- Recurse on the **left** part before the **right** part, and only when the part has at least 2 values (`low < high`).

### Example (lecture array)

```text
a = [8, 7, 6, 1, 0, 9, 2]
quick_sort_trace(a)   →  [2, 0, 3, 5]
a                     →  [0, 1, 2, 6, 7, 8, 9]
```
