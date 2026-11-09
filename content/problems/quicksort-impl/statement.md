The course's Lomuto `partition(array, low, high)` is already loaded (see **Provided code**). It returns the pivot's final index.

Write:

- **`quick_sort(array, low=0, high=None)`**: sort `array[low..high]` **in place** (`high=None` means the last index). Partition, then quicksort the part left of the pivot and the part right of it. Return nothing.
- **`quickselect(array, k, low=0, high=None)`**: return the value that would be at index `k` if the array were sorted (so `k = 0` is the smallest). Partition once; if the pivot landed at `k` you're done, otherwise recurse into **one** side only.

### Examples

```text
a = [8, 7, 6, 1, 0, 9, 2]
quick_sort(a)
a                                   →  [0, 1, 2, 6, 7, 8, 9]

quickselect([8, 7, 6, 1, 0, 9, 2], 3)   →  6
quickselect([8, 7, 6, 1, 0, 9, 2], 0)   →  0
```
