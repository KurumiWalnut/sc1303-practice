`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `min_diff(root)` that returns the **smallest difference** between the values of any two different nodes in a BST with at least two nodes.

### Examples

```text
min_diff([4, 2, 6, 1, 3])                    →  1
min_diff([1, 0, 48, None, None, 12, 49])     →  1
```

### Constraints

- 2 to 5 000 nodes with distinct values.
