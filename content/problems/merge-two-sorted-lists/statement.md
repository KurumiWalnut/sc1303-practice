`list1` and `list2` are the heads of two linked lists, each sorted in ascending order. Write `merge_two_lists(list1, list2)` that merges them into **one sorted list** and returns its head.

**Don't create new nodes.** Re-link the existing ones. A dummy starting node is allowed, as long as it isn't part of the list you return.

> [!PROF-BUG] Week 10 seminar slides, the Node class in exercise 5
>
> The slide's `Node.__init__(self, data=0, next=None)` sets `self.next = None`, so it ignores the `next` you pass in: `Node(1, Node(2))` is just the single node 1. It doesn't break the merge, which only re-links existing nodes, but write `self.next = next` if you build lists with it.

### Examples

```text
1 -> 2 -> 4  and  1 -> 3 -> 4   →   1 -> 1 -> 2 -> 3 -> 4 -> 4
(empty)      and  0             →   0
```

### Constraints

- Each list has up to 30 000 nodes, so use a loop rather than recursion.
