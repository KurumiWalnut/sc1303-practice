`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

The **lowest common ancestor (LCA)** of two nodes is the deepest node that has both of them as descendants. A node counts as a descendant of itself.

Write `lowest_common_ancestor(root, p, q)` that returns the **value** of the LCA of the nodes holding values `p` and `q`. Both values are in the tree.

### Examples

```text
root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
lowest_common_ancestor(root, 2, 8)   →  6
lowest_common_ancestor(root, 2, 4)   →  2     (a node is its own descendant)
```
