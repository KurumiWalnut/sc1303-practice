## Find it first

Deleting starts like a search. Once you find the node, there are three cases.

## Case 1: no children (a leaf)

Just remove it: set the parent's link to `None`.

## Case 2: one child

Remove the node and put its child in its place. The child's whole subtree moves up with it.

## Case 3: two children: use the successor

Replace the deleted node with its **successor**: the smallest value that's bigger than it.

To find the successor:

1. Go to the **right child** of the node you're deleting.
2. Keep going **left** until there's no left child.
3. That node is the successor.

If the successor has a **right child**, that child moves up into the successor's old place. (The successor can't have a left child, otherwise it wouldn't be the leftmost.)

```text
Delete 50:                   Successor = 52 (right once, then left to the bottom)

           50                            52
         /    \                        /    \
       25      75          →         25      75
              /  \                          /  \
            56    89                      56    89
           /  \                          /  \
         52    61                      55    61
           \
            55                  55 (52's right child) takes 52's old place
```

## Recursive delete that returns the new subtree

Writing `delete` so that it **returns the root of the subtree** makes every case short: the parent just stores whatever comes back.

```python
def delete(value, node):
    if node is None:
        return None                              # value isn't in the tree
    if value < node.value:
        node.left_child = delete(value, node.left_child)
        return node
    if value > node.value:
        node.right_child = delete(value, node.right_child)
        return node
    # found it
    if node.left_child is None:                  # 0 or 1 child
        return node.right_child
    if node.right_child is None:
        return node.left_child
    node.right_child = lift(node.right_child, node)   # 2 children
    return node

def lift(node, node_to_delete):
    """Find the successor in this subtree, copy its value up, and remove it."""
    if node.left_child is not None:
        node.left_child = lift(node.left_child, node_to_delete)
        return node
    node_to_delete.value = node.value            # the successor's value moves up
    return node.right_child                      # its right child takes its place
```

Call it as `root = delete(value, root)`. The root itself might be deleted.

## Cost

Finding the node and its successor both walk down the tree: **O(height)**. That's O(log N) for a balanced tree, O(N) for a skewed one.

## Common bugs

- Using the **predecessor** (largest value on the left) when the question expects the successor. Both keep a valid BST, but they give different trees.
- Forgetting the successor's right child, which loses a whole subtree.
- Deleting the root without updating the caller's `root` variable.
- Writing `delete(...)` without assigning its return value to the parent's link.
