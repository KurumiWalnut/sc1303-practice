`Node` (with `value`, `left`, `right` and `height`) and `build_tree` are already loaded (see **Provided code**). `build_tree` takes a level-order list with `None` for a missing child. It **doesn't** fill in `height`, so work heights out from the children instead of reading `node.height`.

Write these four functions using the course's definitions:

- **`height(node)`**: the number of **nodes** on the longest path down from `node`. An empty tree has height 0 and a leaf has height 1.
- **`balance_factor(node)`**: `height(node.right) - height(node.left)`. Negative means left-heavy.
- **`is_balanced(root)`**: `True` if **every** node's balance factor is -1, 0 or +1 (an empty tree is balanced).
- **`imbalance_case(node)`**: if `node`'s balance factor is -2 or less, return `"LL"` when its left child's balance factor is 0 or less, else `"LR"`. If it's +2 or more, return `"RR"` when its right child's balance factor is 0 or more, else `"RL"`. Otherwise return `None`.

### Examples

```text
root = build_tree([30, 20, 40, 10])
height(root)                  →  3
balance_factor(root)          →  -1     (left height 2, right height 1)
is_balanced(root)             →  True

imbalance_case(build_tree([30, 20, None, 10]))         →  "LL"
imbalance_case(build_tree([30, 10, None, None, 20]))   →  "LR"
imbalance_case(build_tree([20, 10, 30]))               →  None
```
