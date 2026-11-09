Write `partition(array, low, high)` using **Hoare's** scheme from the lecture. Work only on `array[low..high]` (inclusive), change it **in place**, and return the pivot's final index.

1. The pivot is the **last** element, `array[high]`.
2. Pointer `a` starts at `low`, and pointer `b` starts at `high - 1`.
3. Move `a` right while `a <= b` and `array[a] <= pivot`. It stops on a value **bigger** than the pivot.
4. Move `b` left while `a <= b` and `array[b] >= pivot`. It stops on a value **smaller** than the pivot.
5. If `a < b`, swap `array[a]` and `array[b]` and go back to step 3. Otherwise the pointers have met or crossed: stop.
6. Swap the pivot into `array[a]` and return `a`.

This is the professor's `hoare_partition` from the Week 9 seminar code. Values **equal** to the pivot don't stop either pointer.

`quick_sort(array, low, high)` is already loaded (see **Provided code**) and uses your `partition`.

### Example (from the lecture)

```text
nums = [8, 7, 6, 1, 0, 9, 2]
partition(nums, 0, 6)   →  2
nums                    →  [0, 1, 2, 7, 8, 9, 6]

partition(nums, 3, 6)   →  3
nums                    →  [0, 1, 2, 6, 8, 9, 7]
```

Lomuto gives `[1, 0, 2, 8, 7, 9, 6]` after the first call, so the tests can tell the two schemes apart.
