`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `sorted_array_to_bst(nums)` that turns a sorted list of distinct numbers into a **height-balanced** BST and returns its root (`None` for an empty list).

Several trees can be correct, so the tests use `check_balanced_bst(root, nums)`, which returns `"ok"` or says what's wrong.

### Example

```text
nums = [-10, -3, 0, 5, 9]
one answer:  [0, -3, 9, -10, None, 5]     another:  [0, -10, 5, None, -3, None, 9]
check_balanced_bst(sorted_array_to_bst(nums), nums)   →  "ok"
```
