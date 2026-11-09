`list1` and `list2` are the heads of two linked lists, each sorted in ascending order. Write `merge_two_lists(list1, list2)` that merges them into **one sorted list** and returns its head.

**Don't create new nodes.** Re-link the existing ones. A dummy starting node is allowed, as long as it isn't part of the list you return.

### Examples

```text
1 -> 2 -> 4  and  1 -> 3 -> 4   →   1 -> 1 -> 2 -> 3 -> 4 -> 4
(empty)      and  0             →   0
```

### Constraints

- Each list has up to 30 000 nodes, so use a loop rather than recursion.
