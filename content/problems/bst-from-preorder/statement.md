`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

`preorder` is the **pre-order traversal** of a BST with distinct values. Write `bst_from_preorder(preorder)` that rebuilds the tree and returns its root.

### Examples

```text
bst_from_preorder([8, 5, 1, 7, 10, 12])   →  [8, 5, 10, 1, 7, None, 12]
bst_from_preorder([1, 3])                 →  [1, None, 3]
```

### Constraints

- 1 to 3 000 distinct values.
