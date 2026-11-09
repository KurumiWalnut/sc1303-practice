`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `remove_leaf_nodes(root, target)` that deletes every **leaf** whose value is `target` and returns the new root. This is a binary tree, not necessarily a BST.

After you delete a leaf, its parent may become a leaf with value `target`. Delete that too, and keep going.

### Examples

```text
remove_leaf_nodes([1, 2, 3, 2, None, 2, 4], 2)    →  [1, None, 3, None, 4]
remove_leaf_nodes([1, 3, 3, 3, 2], 3)             →  [1, 3, None, None, 2]
remove_leaf_nodes([1, 2, None, 2, None, 2], 2)    →  [1]
```
