## Nodes and links

An array stores its values in one block of memory. A **linked list** scatters them: each value lives in its own **node**, and each node holds a **link** to the next node. You only keep a reference to the first node, the **head**. The last node, the **tail**, links to `None`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# once -> upon -> a -> time
head = Node("once")
head.next = Node("upon")
head.next.next = Node("a")
head.next.next.next = Node("time")
```

## Walking the list

Almost every linked-list function starts with this loop:

```python
current = head
while current is not None:
    print(current.data)
    current = current.next
```

## Costs compared with an array

| Operation | Array | Linked list |
|---|---|---|
| Read index *i* | O(1) | O(N): walk from the head |
| Search for a value | O(N) | O(N) |
| Insert / delete at the **front** | O(N): shift everything | **O(1)**: change the head |
| Insert / delete at the end | O(1) | O(N) to find the tail (O(1) if you keep a tail pointer) |
| Insert / delete while walking through | O(N) shift each time | **O(1)** each time |

The last row is the lecture's email-cleaning example. Removing 100 bad addresses from 1 000 takes about 1 100 steps with a linked list, but up to about 100 000 with an array, because of all the shifting.

## Insert and delete

```python
# Insert at the front: O(1)
new_node = Node(value)
new_node.next = head
head = new_node

# Insert after `node`
new_node = Node(value)
new_node.next = node.next
node.next = new_node

# Delete the node after `node`: skip over it
node.next = node.next.next
```

To delete a value, stop at the node **before** it, because a singly linked list can't go backwards. Deleting the head is a special case: return `head.next` as the new head.

## Reversing a list (three pointers)

```python
def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        following = current.next     # remember the rest of the list
        current.next = previous      # flip this link
        previous = current
        current = following
    return previous                  # the old tail is the new head
```

## Two pointers: fast and slow

Move `slow` one step and `fast` two steps at a time.

- When `fast` reaches the end, `slow` is at the **middle**.
- If `fast` ever meets `slow`, the list has a **cycle**.
- To find the **n-th node from the end**, start `fast` n nodes ahead, then move both until `fast` reaches the end.

## Watch out for recursion

Recursive linked-list code is short, but it uses one stack frame per node. Python stops at a depth of about 1 000, so use loops when lists can be long. To print a list backwards, push the values onto a stack (a Python list), then pop them off.

## Common bugs

- Losing the rest of the list by overwriting `current.next` before saving it.
- Forgetting the empty list (`head is None`) or the one-node list.
- Deleting the head without returning the new head to the caller.
- Writing `while current.next` when you meant `while current` (or the other way round). Check which node you need to stop on.
