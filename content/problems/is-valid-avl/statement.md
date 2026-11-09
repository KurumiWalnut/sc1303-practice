`Node` (with `value`, `left`, `right` and `height`) and `build_tree` are already loaded (see **Provided code**). `build_tree` takes a level-order list with `None` for a missing child. It **doesn't** fill in `height`, so work heights out from the children instead of reading `node.height`.

Write `is_valid_avl(root)` that returns `True` if the tree is a valid AVL tree:

1. It's a **BST** with no duplicates: every value in a node's left subtree is smaller than the node, and every value in its right subtree is larger. Check the **whole** subtree, not just the children.
2. **Every** node's balance factor is -1, 0 or +1.

An empty tree is valid.

### Examples

```text
[20, 10, 30]          →  True
[30, 20, None, 10]    →  False   (node 30 has balance factor -2)
[20, 10, 30, 5, 25]   →  False   (25 is in 20's left subtree)
```

### Constraints

- Up to 20 000 nodes.
