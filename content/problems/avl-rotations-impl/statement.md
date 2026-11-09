This is the course's AVL template. `Node`, `_height`, `_update_height`, `_get_balance`, `insert` and `preorder` are already loaded (see **Provided code**), plus two test helpers: `make_node(value, left, right)` builds a node with the right height, and `check_avl(root)` returns `"ok"` or says what's wrong.

Write the two rotations. Each one returns the **new root** of the subtree and must leave correct `height` values on the two nodes that moved:

```text
_rotate_left(x)                       _rotate_right(y)

  x                  y                     y              x
   \                / \                   /              / \
    y       →       x  T3                 x       →      T1  y
   / \               \                   / \                 /
  T2 T3              T2                 T1 T2               T2
```

`insert` calls your rotations to fix LL, RR, LR and RL cases, so once they work every insert keeps the tree balanced.

### Example

```text
x = make_node(10, None, make_node(20, None, make_node(30)))
r = _rotate_left(x)
preorder(r)               →  [20, 10, 30]
(r.height, r.left.height) →  (2, 1)

preorder(build_avl([10, 20, 30]))   →  [20, 10, 30]
```
