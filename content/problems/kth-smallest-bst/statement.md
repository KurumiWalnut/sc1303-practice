`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `kth_smallest(root, k)` that returns the **k-th smallest** value in a BST, counting from 1.

### Examples

```text
kth_smallest([3, 1, 4, None, 2], 1)                     →  1
kth_smallest([5, 3, 6, 2, 4, None, None, 1], 3)         →  3
```

### Constraints

- `1 ≤ k ≤` number of nodes `≤ 5 000`.
