`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `trim_bst(root, low, high)` that removes every node whose value is outside `[low, high]` and returns the new root. Keep the relative structure of the remaining nodes: if a node stays, its remaining descendants stay below it.

### Examples

```text
trim_bst([1, 0, 2], 1, 2)                          →  [1, None, 2]
trim_bst([3, 0, 4, None, 2, None, None, 1], 1, 3)  →  [3, 2, None, 1]
```
