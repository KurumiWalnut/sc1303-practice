`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `balance_bst(root)` that returns the root of a **height-balanced** BST holding the same values as the BST `root`.

The input can be very lopsided.

Several trees can be correct, so the tests use `check_balanced_bst(root, values)`.

### Example

```text
root = [1, None, 2, None, 3, None, 4]     (a chain)
one answer:  [2, 1, 3, None, None, None, 4]
check_balanced_bst(balance_bst(root), [1, 2, 3, 4])   →  "ok"
```

### Constraints

- Up to 20 000 nodes; the input is at most 800 levels deep.
