Complete the `BST` class. It stores integers in a binary search tree built from the provided `TreeNode` class (`value`, `left_child`, `right_child`). `self.root` is `None` when the tree is empty.

- **`insert(value)`**: add `value` to the tree. Smaller values go left, bigger values go right. If `value` is already in the tree, do nothing.
- **`contains(value)`**: return `True` if `value` is in the tree.
- **`inorder()`**: return a list of every value in ascending order.
- **`range_sum(low, high)`**: return the sum of every value `v` with `low ≤ v ≤ high`. For full marks, don't visit subtrees that can't contain values in the range.

### Example

```text
t = BST()
for v in [50, 25, 75, 10, 30, 60, 90, 27]:
    t.insert(v)

t.inorder()          →  [10, 25, 27, 30, 50, 60, 75, 90]
t.contains(27)       →  True
t.contains(55)       →  False
t.range_sum(25, 60)  →  192      (25 + 27 + 30 + 50 + 60)
```

### Constraints

- Up to 5 000 values, inserted in random order.
