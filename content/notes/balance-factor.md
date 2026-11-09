## Why balance matters

A BST is only fast when it's **balanced**. Insert values in sorted order and you get a straight line: height N, so search is O(N). An **AVL tree** (after Adelson-Velsky and Landis) is a BST that **rebalances itself** after every insert or delete, so its height stays about log₂ N.

## Height

The course's AVL template counts **nodes** on the longest path down:

```python
def height(node):
    if node is None:
        return 0                     # empty tree
    return 1 + max(height(node.left), height(node.right))   # a leaf has height 1
```

(Some books count edges instead, so a leaf has height 0. Balance factors come out the same either way.)

## Balance factor

**Course definition:** BF(N) = height(**right** subtree) − height(**left** subtree)

| BF | Meaning |
|---|---|
| −1 | **left-heavy**, still balanced |
| 0 | perfectly balanced |
| +1 | **right-heavy**, still balanced |
| −2 or +2 | **imbalanced**: rotate |

Some sources use left − right, which flips every sign. In this course, **negative means left-heavy**.

## The four imbalance cases

Look at the imbalanced node, then at the child on its heavy side:

| Node BF | Heavy child's BF | Case | Fix |
|---|---|---|---|
| −2 | left child is 0 or −1 | **LL** | single **right** rotation |
| +2 | right child is 0 or +1 | **RR** | single **left** rotation |
| −2 | left child is **+1** | **LR** | rotate left child **left**, then node **right** |
| +2 | right child is **−1** | **RL** | rotate right child **right**, then node **left** |

The name says where the extra height is: for LR, it's in the **L**eft child's **R**ight subtree.

```text
Insert 10, 20, 30 (plain BST):     10  BF +2          RR → rotate 10 left →    20
                                     \                                        /  \
                                     20  BF +1                              10    30
                                       \
                                       30
```

## Checking a whole tree

A tree is balanced only if **every** node's BF is −1, 0 or +1. Checking the root alone isn't enough. Computing `height` again at every node costs O(N log N) on a balanced tree and O(N²) on a skewed one. The fast way returns the height and the "balanced?" answer together in one post-order pass.

## Common bugs

- Using left − right and getting the case names backwards.
- Checking only the root.
- Forgetting that an empty subtree has height 0, so a leaf's BF is 0 − 0 = 0.
