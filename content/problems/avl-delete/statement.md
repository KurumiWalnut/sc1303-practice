The AVL template from the course is already loaded, **with working rotations**: `Node`, `_height`, `_update_height`, `_get_balance`, `_rotate_left`, `_rotate_right`, `insert`, `preorder`, `build_avl(values)` and `check_avl(root)` (see **Provided code**).

Write `delete(root, value)` that removes `value` from the AVL tree and returns the new root. If `value` isn't there, return the tree unchanged.

1. Delete as in a normal BST. A node with **two** children takes the value of its **in-order successor** (the smallest value in its right subtree), and then that successor is deleted from the right subtree.
2. On the way back up, update each node's height and rebalance with the **same rules as `insert`**: left-heavy → LL if the left child's balance factor is `<= 0`, else LR; right-heavy → RR if the right child's balance factor is `>= 0`, else RL.

### Examples

```text
root = build_avl([20, 10, 30, 40])        pre-order [20, 10, 30, 40]
root = delete(root, 10)                   node 20 is now right-heavy (RR)
preorder(root)                            →  [30, 20, 40]

root = build_avl([20, 10, 30, 25, 40])
root = delete(root, 20)                   20 has two children: 25 takes its place
preorder(root)                            →  [25, 10, 30, 40]
```
