Write `partition(array, low, high)` using the **Lomuto** scheme from the lecture. Work only on `array[low..high]` (inclusive), change it **in place**, and return the pivot's final index.

1. The pivot is the **last** element, `array[high]`.
2. A pointer `b` starts at `low`. It marks where the next value smaller than the pivot goes.
3. For each `a` from `low` to `high - 1`: if `array[a] < pivot` (strictly smaller), swap `array[a]` and `array[b]`, then add 1 to `b`.
4. Swap the pivot into `array[b]` and return `b`.

`quick_sort(array, low, high)` is already loaded (see **Provided code**) and uses your `partition`.

### Example (from the lecture)

```text
a = [8, 7, 6, 1, 0, 9, 2]
partition(a, 0, 6)   →  2
a                    →  [1, 0, 2, 8, 7, 9, 6]

b = [1, 7, 4, 1, 10, 9, -2]
quick_sort(b, 0, 6)
b                    →  [-2, 1, 1, 4, 7, 9, 10]
```
