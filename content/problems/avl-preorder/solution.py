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
    x.right = y.left
    y.left = x
    _update_height(x)
    _update_height(y)
    return y


def _rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    _update_height(y)
    _update_height(x)
    return x


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root
    _update_height(root)
    balance = _get_balance(root)
    if balance < -1:
        if _get_balance(root.left) <= 0:
            return _rotate_right(root)            # LL
        root.left = _rotate_left(root.left)       # LR
        return _rotate_right(root)
    if balance > 1:
        if _get_balance(root.right) >= 0:
            return _rotate_left(root)             # RR
        root.right = _rotate_right(root.right)    # RL
        return _rotate_left(root)
    return root


def avl_preorder(values):
    root = None
    for v in values:
        root = insert(root, v)
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        if node is not None:
            out.append(node.value)
            stack.append(node.right)
            stack.append(node.left)
    return out
