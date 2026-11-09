## Rotations keep BST order

A rotation changes the **shape** of a subtree but not its **in-order**, so the BST rule still holds. Each rotation moves a fixed number of links: O(1).

The course template stores `value`, `left`, `right` and `height` on each node (a leaf has height 1):

```python
def _height(n):
    return n.height if n else 0

def _update_height(n):
    n.height = 1 + max(_height(n.left), _height(n.right))
```

## Left rotation (fixes RR)

```text
      x                         y
       \                       / \
        y          →          x   T3
       / \                     \
      T2  T3                   T2
```

```python
def _rotate_left(x):
    y = x.right
    t2 = y.left
    y.left = x          # x drops down to y's left
    x.right = t2        # y's old left subtree moves under x
    _update_height(x)   # x first: it's now below y
    _update_height(y)
    return y            # y is the new root of this subtree
```

## Right rotation (fixes LL)

The mirror image:

```text
        y                     x
       /                     / \
      x          →          T1  y
     / \                       /
    T1  T2                    T2
```

## Double rotations

- **LR** (node BF −2, left child BF +1): `node.left = _rotate_left(node.left)`, then `return _rotate_right(node)`.
- **RL** (node BF +2, right child BF −1): `node.right = _rotate_right(node.right)`, then `return _rotate_left(node)`.

The first rotation turns the zig-zag into a straight line. The second one balances it.

## AVL insert = BST insert + rebalance on the way up

```python
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root                          # no duplicates
    _update_height(root)
    balance = _height(root.right) - _height(root.left)
    if balance < -1:                         # left-heavy
        if _get_balance(root.left) <= 0:
            return _rotate_right(root)       # LL
        root.left = _rotate_left(root.left)  # LR
        return _rotate_right(root)
    if balance > 1:                          # right-heavy
        if _get_balance(root.right) >= 0:
            return _rotate_left(root)        # RR
        root.right = _rotate_right(root.right)   # RL
        return _rotate_left(root)
    return root
```

Each recursive call **returns the (possibly new) root** of its subtree, and the parent stores it. That's how a rotation deep in the tree gets linked back in. Always call `root = insert(root, value)`.

## Worked examples (from the template)

| Insert order | Case at the root | Result (pre-order) |
|---|---|---|
| 10, 20, 30 | RR → rotate left | 20, 10, 30 |
| 30, 20, 10 | LL → rotate right | 20, 10, 30 |
| 30, 10, 20 | LR → left, then right | 20, 10, 30 |
| 10, 30, 20 | RL → right, then left | 20, 10, 30 |

## Cost

The height stays O(log N), so search, insert and delete are all **O(log N)**, whatever order the data arrives in.

## Common bugs

- Updating heights in the wrong order: update the node that moved **down** first.
- Forgetting to return the new root from a rotation, or not storing it in the parent.
- Mixing up the BF sign: in this course, negative means left-heavy.
