Write `avl_preorder(values)`: insert the values one at a time into an empty AVL tree and return the tree's **pre-order** traversal (root, left subtree, right subtree) as a list.

Nothing is provided this time: write the node class, heights, both rotations and the rebalancing insert yourself, the way the course template does. Use the same rules:

- Ignore duplicates.
- Balance factor = height(right) - height(left).
- Left-heavy (`< -1`): **LL** (single right rotation) if the left child's balance factor is `<= 0`, otherwise **LR**.
- Right-heavy (`> 1`): **RR** (single left rotation) if the right child's balance factor is `>= 0`, otherwise **RL**.

### Examples

```text
avl_preorder([10, 20, 30])                →  [20, 10, 30]
avl_preorder([1, 2, 3, 4, 5, 6, 7])       →  [4, 2, 1, 3, 6, 5, 7]
avl_preorder([])                          →  []
```

### Constraints

- Up to 15 000 values.
