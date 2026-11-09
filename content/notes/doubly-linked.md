## Two links per node

In a **doubly linked list**, each node links to the **next** node *and* the **previous** node. The list keeps references to both its **head** and its **tail**.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

Because you can reach both ends in one step, adding or removing at **either** end is O(1).

## Append at the tail: O(1)

```python
def append(self, value):
    node = Node(value)
    if self.tail is None:            # empty list: the node is both ends
        self.head = self.tail = node
    else:
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
```

## Remove from the head: O(1)

```python
def pop_front(self):
    if self.head is None:
        return None
    node = self.head
    self.head = node.next
    if self.head is None:            # the list is now empty
        self.tail = None
    else:
        self.head.prev = None
    return node.data
```

## The perfect queue

A queue adds at the back and removes from the front.

| Structure | Add at the back | Remove from the front |
|---|---|---|
| Python list | O(1) `append` | **O(N)** `pop(0)` shifts everything |
| Singly linked list (head only) | O(N) walk to the tail | O(1) |
| **Doubly linked list** | **O(1)** | **O(1)** |

That's why the lecture recommends a doubly linked list for queues. Python's `collections.deque` is built on the same idea.

## Removing a node from the middle

If you already hold a reference to the node, you can unlink it in O(1) without walking the list:

```python
node.prev.next = node.next
node.next.prev = node.prev
```

Check for `None` first: the node might be the head or the tail.

## Where it's used: LRU cache

A **least-recently-used cache** combines a dict (key → node, for O(1) lookup) with a doubly linked list ordered from most to least recently used. On each access, move the node to the front. When the cache is full, remove the tail. Every operation is O(1).

## Common bugs

- Updating `next` but forgetting `prev` (or the other way round). Walk the list backwards from the tail to check.
- Forgetting to set `tail = None` (or `head = None`) when the last node is removed.
- Not handling the first `append` into an empty list, where the new node is both the head and the tail.
