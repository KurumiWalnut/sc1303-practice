`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `invert_tree(root)` that mirrors the tree (swaps every node's left and right children) and returns the root.

### Examples

```text
invert_tree([4, 2, 7, 1, 3, 6, 9])   →  [4, 7, 2, 9, 6, 3, 1]
invert_tree([2, 1, 3])               →  [2, 3, 1]
invert_tree([])                      →  []
```
