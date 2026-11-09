## Visiting every node

A **traversal** visits every node once. **Depth-first** traversals go down one branch as far as possible before trying the next. They differ only in **when** you visit the node itself compared with its subtrees:

| Traversal | Order | Use it for |
|---|---|---|
| **In-order** | left, **node**, right | a BST's values in **sorted order** |
| **Pre-order** | **node**, left, right | copying or saving a tree (the root comes first) |
| **Post-order** | left, right, **node** | deleting or sizing a tree (the children come first) |

```text
              F
            /   \
          B       G             In-order:   A B C D E F G H I
         / \       \            Pre-order:  F B A D C E G I H
        A   D       I           Post-order: A C E D B H I G F
           / \     /
          C   E   H
```

```python
def inorder(node, out):
    if node is None:
        return
    inorder(node.left_child, out)
    out.append(node.value)          # move this line to get pre- or post-order
    inorder(node.right_child, out)
```

## Breadth-first (level order)

Visit the tree level by level using a **queue**, just like BFS on a graph:

```python
from collections import deque

def level_order(root):
    if root is None:
        return []
    levels, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):           # everything currently queued is one level
            node = queue.popleft()
            level.append(node.value)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)
        levels.append(level)
    return levels
```

## Validating a BST

Checking only each node against its own children **isn't enough**:

```text
      5
     / \
    4   6        Every parent/child pair looks fine, but 3 is in 5's RIGHT subtree,
       / \       so it must be bigger than 5. This is NOT a valid BST.
      3   7
```

Pass down the allowed range instead. Every node must sit strictly between a `low` and a `high` bound:

```python
def is_valid_bst(node, low=None, high=None):
    if node is None:
        return True
    if (low is not None and node.value <= low) or (high is not None and node.value >= high):
        return False
    return (is_valid_bst(node.left_child, low, node.value) and
            is_valid_bst(node.right_child, node.value, high))
```

Another way: an in-order traversal of a valid BST is **strictly increasing**.

## Recursive tree patterns

Many tree questions follow the same shape: solve the problem for the left and right subtrees, then combine the answers.

```python
def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left_child), max_depth(node.right_child))
```

All traversals are **O(N)**: each node is visited once.

## Common bugs

- Forgetting the `None` base case.
- Building a new list in every recursive call and throwing it away. Pass one list down, or return and join the lists.
- Validating with parent/child checks only (see above).
