Write a class `MinHeap` stored in a list `self.heap` (index 0 is the root, the children of `i` are `2i + 1` and `2i + 2`):

- **`insert(value)`**: append, then **trickle up** while the value is smaller than its parent.
- **`delete()`**: remove and return the **smallest** value (`None` if empty). Move the last value to the root, then **trickle down**, always swapping with the **smaller** child.
- **`peek()`**: the smallest value, or `None`.

### Example

```text
h = MinHeap()
for v in [30, 20, 15, 50, 10]: h.insert(v)
h.heap       →  [10, 15, 20, 50, 30]
h.delete()   →  10
h.heap       →  [15, 30, 20, 50]
```
