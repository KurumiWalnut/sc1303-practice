Complete the `DoublyLinkedList` class. It uses the provided `Node` class (`data`, `next`, `prev`) and keeps references to both `self.head` and `self.tail`.

| Method | What it does |
|---|---|
| `append(value)` | add `value` at the tail, **O(1)** |
| `prepend(value)` | add `value` at the head, **O(1)** |
| `pop_front()` | remove the head and return its value (`None` if empty), **O(1)** |
| `pop_back()` | remove the tail and return its value (`None` if empty), **O(1)** |
| `to_list()` | values from head to tail (follow `next`) |
| `to_list_reversed()` | values from tail to head (follow `prev`) |
| `__len__()` | the number of nodes |

Keep both links of every node correct: the tests walk the list in both directions. When the list becomes empty, set both `head` and `tail` to `None`.

### Example

```text
d = DoublyLinkedList()
for v in [1, 2, 3, 4]:
    d.append(v)
d.to_list()            →  [1, 2, 3, 4]
d.to_list_reversed()   →  [4, 3, 2, 1]
d.pop_front()          →  1
d.pop_back()           →  4
d.to_list()            →  [2, 3]
len(d)                 →  2
```
