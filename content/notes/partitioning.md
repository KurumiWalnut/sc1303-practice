## What partitioning does

Pick one value, the **pivot**, and rearrange the (sub)array so that:

- everything **smaller** than the pivot is on its left,
- everything **larger** is on its right,
- the pivot sits **between** them, which is exactly where it will be once the array is sorted.

The two sides don't have to be sorted. Quicksort and quickselect are both built on this one step.

## Lomuto partition (lecture and Week 9 exercise)

1. Pivot = the **last** element, `array[high]`.
2. Pointer `b` marks where the next smaller value should go. It starts at `low`.
3. Scan `a` from `low` to `high - 1`. If `array[a] < pivot`, swap `array[a]` with `array[b]` and move `b` on by one.
4. Finally swap the pivot into `array[b]` and return `b`.

```python
def partition(array, low, high):
    pivot = array[high]
    b = low                               # the first slot that isn't known to be smaller
    for a in range(low, high):
        if array[a] < pivot:              # strictly smaller, as in the lecture
            array[a], array[b] = array[b], array[a]
            b += 1
    array[b], array[high] = array[high], array[b]   # drop the pivot into place
    return b
```

## Worked example (lecture, Lomuto)

```text
[8, 7, 6, 1, 0, 9, 2]     pivot = 2, b = 0
 a=0..2: 8, 7, 6 are not < 2
 a=3: 1 < 2 → swap with index 0  → [1, 7, 6, 8, 0, 9, 2], b = 1
 a=4: 0 < 2 → swap with index 1  → [1, 0, 6, 8, 7, 9, 2], b = 2
 a=5: 9 is not < 2
 swap pivot into index 2         → [1, 0, 2, 8, 7, 9, 6]   return 2
```

2 is now in its final place. Next you'd partition `[1, 0]` and `[8, 7, 9, 6]`.

## Hoare partition (the lecture version)

The lecture covers Hoare as fully as Lomuto. It makes **fewer swaps**, so it's usually faster, but it's **harder to code**. The Week 9 coding exercise was Lomuto, but you should be able to trace and write both.

1. Pivot = the **last** element, `array[high]`, as in Lomuto.
2. Two pointers: `a` starts at `low`, and `b` starts at `high - 1`, just left of the pivot.
3. Move `a` right until it's on a value **≥ pivot**.
4. Move `b` left until it's on a value **≤ pivot**, or it reaches `a`.
5. If the pointers have met or crossed (`a >= b`), stop. Otherwise swap `array[a]` with `array[b]`, move `a` on by one, and go back to step 3.
6. Swap the pivot into `array[a]` and return `a`.

```python
def partition(array, low, high):
    pivot = array[high]
    a, b = low, high - 1
    while True:
        while array[a] < pivot:              # the pivot itself stops a, at high at the latest
            a += 1
        while b > a and array[b] > pivot:
            b -= 1
        if a >= b:                           # the pointers have met
            break
        array[a], array[b] = array[b], array[a]
        a += 1
    array[a], array[high] = array[high], array[a]   # drop the pivot into place
    return a
```

It returns the pivot's final index, just like Lomuto, so `quick_sort` doesn't change.

## Worked example (lecture, Hoare)

```text
[8, 7, 6, 1, 0, 9, 2]     pivot = 2, a = 0, b = 5
 a stops at once on 8 (index 0)
 b moves past 9, stops on 0 (index 4)
 swap them, a moves on         → [0, 7, 6, 1, 8, 9, 2], a = 1
 a stops on 7 (index 1)
 b moves past 8, stops on 1 (index 3)
 swap them, a moves on         → [0, 1, 6, 7, 8, 9, 2], a = 2
 a stops on 6 (index 2)
 b moves past 7 and reaches a  → the pointers have met
 swap pivot into index 2       → [0, 1, 2, 7, 8, 9, 6]   return 2
```

The pivot ends up at index 2 with both schemes, but the other values are in a different order. Lomuto gave `[1, 0, 2, 8, 7, 9, 6]`. That's how a trace question can tell which scheme you used.

Quicksort then partitions `[7, 8, 9, 6]` (`low = 3`): `a` stops on 7 at once, `b` moves past 9 and 8 to meet it, and 6 swaps with 7. The array goes `[0, 1, 2, 6, 8, 9, 7]` → `[0, 1, 2, 6, 7, 9, 8]` → `[0, 1, 2, 6, 7, 8, 9]`.

## Lomuto vs Hoare

| | Lomuto | Hoare |
|---|---|---|
| Pointers | `a` scans, `b` marks the boundary; both move right | `a` from the left, `b` from the right, towards each other |
| Swaps when | `array[a] < pivot` | both pointers have stopped and haven't met |
| Values equal to the pivot | end up on its right | can end up on either side |
| Swaps made | more | fewer, so usually faster |
| Code | simpler | trickier (when to stop each pointer) |

## Other partitions you'll meet

| Problem | Idea |
|---|---|
| Evens before odds | Lomuto with "is even" instead of `< pivot` |
| Three groups (0s, 1s, 2s) | **Dutch national flag**: three pointers `low`, `mid`, `high` |
| Keep the original order in each group | **Stable** partition: build three lists (less, equal, greater) and join them; O(N) extra space |

## Cost

One pass over the subarray, so **O(N)** time and O(1) extra space for the in-place versions.

## Common bugs

Lomuto:

- Starting `b` at 0 instead of `low` when partitioning a subarray.
- Looping `a` up to `high` inclusive, which compares the pivot with itself.
- Forgetting the final swap, or returning `high` instead of `b`.
- Using `<=` when the question says `<`. With repeated values, that puts them on a different side.

Hoare:

- Starting `b` at `high`, on the pivot itself, instead of `high - 1`.
- Moving `a` on while `array[a] <= pivot`. Then nothing stops it at the pivot, and it runs past `high`.
- Not moving `a` on after a swap. If both values equal the pivot, they swap with each other forever.
- Returning `b` instead of `a`. The pivot goes where `a` stopped.
