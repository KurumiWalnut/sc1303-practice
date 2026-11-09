`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write these functions from the course template:

- **`search(search_value, node)`**: return the **node** holding `search_value`, or `None` if it isn't in the tree.
- **`insert(value, node)`**: insert `value` into the BST whose root is `node` (never `None`). If the value is already there, do nothing.
- **`max_value(node)`** and **`min_value(node)`**: the largest and smallest values in the tree. (The template calls it `max`, but that hides Python's built-in `max`.)

Each step should go down **one** branch: don't visit the whole tree.

### Example

```text
root = TreeNode(50)
for v in [30, 70, 20, 40, 60, 80]:
    insert(v, root)
tree_to_list(root)         →  [50, 30, 70, 20, 40, 60, 80]
search(40, root).value     →  40
search(45, root)           →  None
max_value(root)            →  80
```
