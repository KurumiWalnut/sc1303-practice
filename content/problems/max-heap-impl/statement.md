Complete `insert` and `delete` in the `MaxHeap` class (from `Heap_template.py`). The heap is stored in the list `self.heap`, with the root at index `0`.

**`insert(value)`**
1. Append `value` to the end of `self.heap`. It becomes the last node.
2. *Trickle up:* while it's bigger than its parent, swap it with the parent.

**`delete()`** removes and returns the largest value.
1. If the heap is empty, return `None`.
2. Remember the root, then move the last node into the root's place.
3. *Trickle down:* while that value has a child bigger than it, swap it with the **bigger** child.

Both operations must be **O(log N)**. The tests check the exact contents of `self.heap`, so follow these steps exactly. In particular, only swap when the value is strictly bigger.

### Example

```text
h = MaxHeap()
for v in [30, 20, 15, 50, 10, 8, 16, 60]:
    h.insert(v)
h.heap      →  [60, 50, 16, 30, 10, 8, 15, 20]
h.delete()  →  60
h.heap      →  [50, 30, 16, 20, 10, 8, 15]
```

The helpers `_parent(i)`, `_left(i)` and `_right(i)` give you the index formulas.
