The tests drive your class through `run_ops` (see **Provided code**).

Write a class `MyQueue` that behaves like a queue (first in, first out), using **only two stacks**: two lists where you only ever `append`, `pop()` from the end, look at `[-1]` or check the length.

- **`push(x)`**: add `x` to the back.
- **`pop()`**: remove and return the front value.
- **`peek()`**: return the front value.
- **`empty()`**: `True` if the queue is empty.

`pop` and `peek` are only called when the queue isn't empty.

### Example

```text
push(1), push(2)
peek()    →  1
pop()     →  1
empty()   →  False
```
