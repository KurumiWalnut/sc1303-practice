`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write `delete(value, node)` that deletes `value` from the BST rooted at `node` and **returns the new root** of that subtree. It's called as `root = delete(value, root)`.

Follow the lecture's rules exactly, because the tests check the shape of the tree:

1. **No children:** remove the node.
2. **One child:** the child takes the node's place.
3. **Two children:** replace the node with its **successor**: go to the right child, then left as far as possible. If the successor has a right child, that child takes the successor's old place.

If `value` isn't in the tree, return the tree unchanged.

### Example

```text
root = build_bst([50, 25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95])
root = delete(56, root)      # two children: successor is 61
tree_to_list(root)   →  [50, 25, 75, 10, 33, 61, 89, 4, 11, 30, 40, 52, None, 82, 95]
```
