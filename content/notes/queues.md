## First in, first out

A **queue** is a line at a shop: items join at the **back** and leave from the **front** (**FIFO**). Only the front item can be read.

| Operation | Meaning | `collections.deque` | Plain list |
|---|---|---|---|
| enqueue | add to the back | `q.append(x)`: O(1) | `append`: O(1) |
| dequeue | remove from the front | `q.popleft()`: **O(1)** | `pop(0)`: **O(N)** |
| read | look at the front | `q[0]`: O(1) | `q[0]`: O(1) |

`list.pop(0)` shifts every remaining element left by one. With 100 000 items, a loop of `pop(0)` calls does billions of moves. Use `deque`.

```python
from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft() if self.data else None

    def read(self):
        return self.data[0] if self.data else None
```

## When to reach for a queue

- Handling things **in the order they arrived**: print jobs, requests, BFS.
- **Simulations** where items rotate: take from the front, put it at the back.
- **First non-repeating character** (Week 8, exercise 4): count characters in a dict, and keep a queue of candidates in order. Drop from the front any whose count is now more than 1.

## A queue from two stacks

Push onto an **in** stack. To dequeue, pop from an **out** stack, and when **out** is empty, first move everything from **in** to **out** (that reverses the order). Each item is moved at most once, so each operation is **O(1) amortised**.

## Deque tricks: the sliding window maximum

A `deque` can add and remove at **both** ends in O(1). For the maximum of every window of size `k`, keep a deque of indexes whose values are **decreasing**:

1. Pop from the **back** any index whose value is ≤ the new value. They can never be the maximum again.
2. Append the new index.
3. Pop from the **front** if that index has slid out of the window.
4. The front is the current window's maximum.

Each index enters and leaves once: O(N) in total, instead of O(N·k).

## Common bugs

- `list.pop(0)` in a loop: correct, but too slow for big inputs.
- Removing from an empty queue without checking.
- In the two-stack queue, moving items into **out** when it isn't empty. That mixes up the order.
