`TreeNode` (with `value`, `left_child`, `right_child`) and the helpers `build_tree`, `tree_to_list`, `build_bst` and `inorder_values` are already loaded (see **Provided code**). Trees in the examples are written in level order, with `None` for a missing child.

Write these functions. Each traversal returns a **list of values** (an empty tree gives `[]`):

- `inorder(node)`: left subtree, node, right subtree
- `preorder(node)`: node, left subtree, right subtree
- `postorder(node)`: left subtree, right subtree, node
- `is_valid_bst(node)`: `True` if the tree is a valid BST: every value in a node's left subtree is **strictly smaller**, and every value in its right subtree **strictly bigger**. An empty tree is valid.

### Examples

```text
root = build_tree(['F', 'B', 'G', 'A', 'D', None, 'I', None, None, 'C', 'E', 'H'])
inorder(root)     →  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
preorder(root)    →  ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
postorder(root)   →  ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']

is_valid_bst(build_tree([2, 1, 3]))                    →  True
is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))  →  False
```
