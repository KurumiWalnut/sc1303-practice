`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `max_depth(root)` that returns the number of nodes on the **longest path** from the root down to a leaf. An empty tree has depth 0.

### Examples

```text
max_depth([3, 9, 20, None, None, 15, 7])   →  3
max_depth([1, None, 2])                    →  2
max_depth([])                              →  0
```
