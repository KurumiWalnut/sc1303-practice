## Priority queues

A **priority queue** always hands out the most important item first, whatever order the items arrived in. Think of a hospital A&E queue, where the most urgent patient is seen next.

| Implementation | Insert | Remove the highest priority |
|---|---|---|
| Ordered array | O(N): shift to keep it sorted | O(1) |
| **Max-heap** | **O(log N)** | **O(log N)** |

A heap wins because both operations stay fast.

## The two heap rules (max-heap)

1. **Heap condition:** every node is bigger than all of its descendants, so the root is always the largest value.
2. **Complete tree:** every level is full except possibly the bottom one, which fills from the left with no gaps.

The rightmost node on the bottom level is the **last node**.

Unlike a BST, a heap has no "left < right" rule. It's only *weakly* ordered, so you can't search it quickly. It does one job well: give you the maximum.

## Stored in an array

Read the tree level by level, from left to right:

```text
            60
         /      \
       50        16
      /  \      /  \
    30    10   8    15
   /
 20                      →   [60, 50, 16, 30, 10, 8, 15, 20]
```

For the node at index `i`:

| | Index |
|---|---|
| Parent | `(i - 1) // 2` |
| Left child | `2 * i + 1` |
| Right child | `2 * i + 2` |
| Root | `0` |
| Last node | `len(heap) - 1` |

## Insert: trickle up, O(log N)

1. Append the value to the end of the array, so it becomes the new last node.
2. While it's bigger than its parent, swap the two.

```python
def insert(self, value):
    self.heap.append(value)
    i = len(self.heap) - 1
    while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
        parent = (i - 1) // 2
        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
        i = parent
```

## Delete: trickle down, O(log N)

You always delete the **root**, which holds the maximum.

1. Remember the root's value.
2. Move the last node into the root's place.
3. While the moved value has a child bigger than it, swap it with the **bigger** child.

Always swap with the bigger child. If you swap with the smaller one, the bigger child ends up below a smaller parent and breaks the heap condition.

## Why use the last node?

It keeps the tree **complete**. Inserting at the last spot fills the next gap, and removing the last node leaves no hole. In an array, both are O(1) (`append` and `pop`).

## Python's `heapq`

`heapq` turns a plain list into a **min**-heap with `heappush`, `heappop` and `heapify`. For a max-heap, push negative values (`heappush(h, -x)`) and negate them again when you pop.

## Common bugs

- Off-by-one child indexes (`2 * i` instead of `2 * i + 1`).
- Comparing with a child without first checking that it exists (`left < len(heap)`).
- Deleting from a one-element heap: pop the last value and return it straight away. Don't move it back to the root.

## Heaps in bigger problems

**Merging k sorted lists.** Put the first value of each list in a min-heap, as `(value, which list, index)`. Pop the smallest, add it to the output, and push the next value from the same list. The heap never holds more than k entries, so merging N values costs **O(N log k)**.

**Running median: two heaps.** Keep the smaller half of the numbers in a **max-heap** and the larger half in a **min-heap**, with sizes equal or the max-heap one bigger. The median is the max-heap's top, or the average of the two tops. Each new number costs O(log N):

1. Push it into the max-heap (the lower half).
2. Move the max-heap's top to the min-heap, so everything in the lower half stays ≤ everything in the upper half.
3. If the min-heap is now bigger, move its top back.

**Top k.** To keep the k **largest** values seen so far, use a **min**-heap of size k: its root is the smallest of the top k, so it's the one to drop when a bigger value arrives.
