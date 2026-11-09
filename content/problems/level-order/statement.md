`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `level_order(root)` that returns the values level by level, from top to bottom and left to right, as a **list of lists**.

### Examples

```text
level_order([3, 9, 20, None, None, 15, 7])   →  [[3], [9, 20], [15, 7]]
level_order([1])                             →  [[1]]
level_order([])                              →  []
```
