The tests drive your class through `run_ops` (see **Provided code**).

Write a class `MinStack` where **every** operation is O(1):

- **`push(val)`**, **`pop()`** (removes the top) and **`top()`** (returns it), as for a normal stack,
- **`get_min()`**: return the **smallest** value currently in the stack.

`pop`, `top` and `get_min` are only called when the stack isn't empty.

### Example

```text
push(-2), push(0), push(-3)
get_min()   →  -3
pop()
top()       →  0
get_min()   →  -2
```
