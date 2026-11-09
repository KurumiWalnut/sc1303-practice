The course's `Node` class is already loaded. Each node has `data` and `next`. The helpers `build_list` and `to_pylist` are there too (see **Provided code**).

Write these five functions. Each takes the `head` of a list, which is `None` for an empty list:

| Function | Returns |
|---|---|
| `to_list(head)` | a Python list of the values, from head to tail |
| `append(head, value)` | the head, after adding `value` at the **tail** |
| `prepend(head, value)` | the new head, after adding `value` at the **front** |
| `delete_value(head, value)` | the head, after removing the **first** node holding `value` (unchanged if it isn't there) |
| `reversed_values(head)` | a Python list of the values from tail to head, using a **stack** |

Change the existing nodes; don't build a new list. Use loops rather than recursion, because lists can have 50 000 nodes.

### Examples

```text
head = build_list(["once", "upon", "a", "time"])
to_list(head)                       →  ['once', 'upon', 'a', 'time']
to_list(append(head, "in"))         →  ['once', 'upon', 'a', 'time', 'in']
to_list(prepend(head, "and"))       →  ['and', 'once', 'upon', 'a', 'time', 'in']
to_list(delete_value(head, "a"))    →  ['once', 'upon', 'time', 'in']
reversed_values(build_list([1, 2, 3]))  →  [3, 2, 1]
```
