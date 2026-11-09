## Measuring speed in steps

The course measures an operation by **how many steps** it takes, not by seconds, because steps don't depend on the computer. The four basic array operations:

| Operation | Steps for an array of N items | Why |
|---|---|---|
| **Read** `arr[i]` | **1** | the address is the start address + i |
| **Search** for a value | up to **N** | linear search checks each cell in turn |
| **Insert** at the end | **1** | nothing to move |
| **Insert** at index i | **N − i shifts + 1** | everything from i onwards moves right one place; at the front that's **N + 1** |
| **Delete** at index i | **1 + (N − i − 1) shifts** | the gap is closed by moving everything after it left; at the front that's **N** |

## Linear search with a step count

```python
def linear_search(arr, target):
    steps = 0
    for i, value in enumerate(arr):
        steps += 1                     # one comparison
        if value == target:
            return i, steps
    return -1, steps                   # checked all N cells
```

`linear_search([10, 20, 30, 40, 50], 30)` returns `(2, 3)`: found at index 2 after 3 comparisons.

## Inserting by hand

`list.insert` hides the shifting. Written out:

```python
def insert_at(arr, index, value):
    arr.append(None)                   # make room at the end
    shifts = 0
    for j in range(len(arr) - 1, index, -1):
        arr[j] = arr[j - 1]            # move right, starting from the back
        shifts += 1
    arr[index] = value
    return shifts
```

Shift from the **back**. Going from the front overwrites values before they've been moved.

## Inserting into a set

A **set** (in the array sense) never holds duplicates, so every insert first **searches** the whole array for the value: up to N steps, then the insert. Inserting at the end costs N + 1 steps; at the front it's 2N + 1.

## Two-pointer tricks

Many array questions need only **two indexes** moving through the list:

- **Reverse in place:** swap `arr[left]` and `arr[right]`, then move both inwards. That's N/2 swaps.
- **Remove a value in place:** a "write" index trails a "read" index, copying across only the values to keep.
- **Rotate by k:** reverse the whole array, then reverse the first k and the last N − k.

## Prefix and suffix products

*Product of Array Except Self* without division: `answer[i]` = (product of everything on the left of i) × (product of everything on the right). Fill the left products in a forward pass, then multiply in the right products in a backward pass: O(N).
