`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `is_balanced(root)` that returns `True` if, at **every** node, the heights of the left and right subtrees differ by at most 1.

### Examples

```text
[3, 9, 20, None, None, 15, 7]          →  True
[1, 2, 2, 3, 3, None, None, 4, 4]      →  False
[]                                     →  True
```

### Constraints

- Up to 30 000 nodes, and the tree is at most 800 levels deep.
