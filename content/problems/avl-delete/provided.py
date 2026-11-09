class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # leaf height = 1


def _height(n):
    return n.height if n else 0


def _update_height(n):
    n.height = 1 + max(_height(n.left), _height(n.right))


def _get_balance(n):
    return _height(n.right) - _height(n.left) if n else 0


def _rotate_left(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    _update_height(x)
    _update_height(y)
    return y


def _rotate_right(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    _update_height(y)
    _update_height(x)
    return x


def insert(root, value):
    """Insert a value into the AVL tree and return the new root (the course template)."""
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root                               # no duplicates
    _update_height(root)
    balance = _get_balance(root)
    if balance < -1:                              # left-heavy
        if _get_balance(root.left) <= 0:
            return _rotate_right(root)            # LL
        root.left = _rotate_left(root.left)       # LR
        return _rotate_right(root)
    if balance > 1:                               # right-heavy
        if _get_balance(root.right) >= 0:
            return _rotate_left(root)             # RR
        root.right = _rotate_right(root.right)    # RL
        return _rotate_left(root)
    return root


def preorder(n):
    """Values in pre-order (root, left subtree, right subtree)."""
    out, stack = [], [n]
    while stack:
        node = stack.pop()
        if node is not None:
            out.append(node.value)
            stack.append(node.right)
            stack.append(node.left)
    return out


def make_node(value, left=None, right=None):
    """Build a node with its height set correctly from its children."""
    n = Node(value)
    n.left, n.right = left, right
    _update_height(n)
    return n


def build_avl(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def check_avl(root):
    """Return "ok" if root is a BST with correct stored heights and every balance factor in -1..1."""
    order, stack, node = [], [], root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        order.append(node.value)
        node = node.right
    for a, b in zip(order, order[1:]):
        if not a < b:
            return f"not a BST: the in-order traversal has {a} before {b}"
    nodes, stack = [], [root] if root is not None else []
    while stack:
        node = stack.pop()
        nodes.append(node)
        for child in (node.left, node.right):
            if child is not None:
                stack.append(child)
    for node in reversed(nodes):                  # children come before their parents
        hl, hr = _height(node.left), _height(node.right)
        if node.height != 1 + max(hl, hr):
            return f"node {node.value} has height {node.height}, but it should be {1 + max(hl, hr)}"
        if abs(hr - hl) > 1:
            return f"node {node.value} is unbalanced (balance factor {hr - hl})"
    return "ok"
