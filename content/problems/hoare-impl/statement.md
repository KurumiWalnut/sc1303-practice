Write `partition(array, low, high)` using **Hoare's** scheme from the lecture. Work only on `array[low..high]` (inclusive), change it **in place**, and return the pivot's final index.

1. The pivot is the **last** element, `array[high]`.
2. Pointer `a` starts at `low`, and pointer `b` starts at `high - 1`.
3. Move `a` right until `array[a] >= pivot`.
4. Move `b` left until `array[b] <= pivot`, or until `b` reaches `a`.
5. If `a >= b`, the pointers have met: stop. Otherwise swap `array[a]` and `array[b]`, add 1 to `a` (not `b`), and go back to step 3.
6. Swap the pivot into `array[a]` and return `a`.

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
