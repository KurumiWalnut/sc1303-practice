## The BST rules

A **binary search tree** is a tree of nodes where:

- each node has at most two children, a **left** child and a **right** child;
- every value in a node's **left** subtree is **smaller** than the node;
- every value in a node's **right** subtree is **bigger** than the node.

Some vocabulary: **root** (the top node), **parent**, **children**, **descendants**, **ancestors**, **leaf** (a node with no children), **level** (a row of the tree), **height** (the number of levels).

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
```

## Search: follow one path down

At each node: if it's the value, stop. If the value is smaller, go left; if it's bigger, go right. If you fall off the bottom (`None`), the value isn't in the tree.

```python
def search(search_value, node):
    if node is None or node.value == search_value:
        return node                    # found it, or reached the bottom
    if search_value < node.value:
        return search(search_value, node.left_child)
    return search(search_value, node.right_child)
```

## Insert: search for where it should be, then attach it

```python
def insert(value, node):
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)
    elif value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)
    # equal: already in the tree, do nothing
```

New values always become **leaves**.

## Min and max

The smallest value is the **leftmost** node; the largest is the **rightmost**. Keep following one side until the next child is `None`.

## How fast?

Each step goes down one level, so search and insert cost **O(height)**.

| Tree shape | Height | Search / insert |
|---|---|---|
| Balanced (each level full) | about log₂ N | **O(log N)** |
| Skewed (values inserted already sorted) | N | **O(N)**, as slow as a linked list |

The order of insertion decides the shape. Inserting 1, 2, 3, 4, 5 gives a straight line to the right. AVL trees (Week 12) fix this by rebalancing.

## BST vs ordered array

| | Ordered array | Balanced BST |
|---|---|---|
| Search | O(log N) binary search | O(log N) |
| Insert / delete | O(N): shift elements | **O(log N)** |

## Common bugs

- Comparing with the wrong child: smaller goes **left**.
- Forgetting the `None` checks before going down a side.
- Returning nothing from a recursive `search`: you need `return search(...)`, not just `search(...)`.
- Assuming O(log N) when the tree could be skewed.
