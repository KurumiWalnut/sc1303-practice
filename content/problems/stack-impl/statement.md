Write a `Stack` class backed by a Python list, using the **end** of the list as the top:

- **`push(value)`**: add to the top.
- **`pop()`**: remove and return the top value, or `None` if the stack is empty.
- **`read()`**: return the top value without removing it, or `None` if empty.
- **`is_empty()`**: `True` if there's nothing in it.
- **`__len__()`**: how many values it holds.

Then use your stack to write **`reverse_string(s)`**: push every character, then pop them all off.

All the stack operations should be O(1). `insert(0, ...)` and `pop(0)` are O(N).

### Example

```text
s = Stack()
s.push(1); s.push(2); s.push(3)
s.read()     →  3
s.pop()      →  3
s.pop()      →  2
len(s)       →  1
reverse_string("abc")   →  "cba"
```
