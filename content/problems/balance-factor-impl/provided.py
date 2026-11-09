class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1  # leaf height = 1 (build_tree doesn't update this)


def build_tree(values):
    """Level-order list -> tree of Node. None marks a missing child, e.g. [30, 20, 40, 10]."""
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue, i, pos = [root], 1, 0
    while i < len(values):
        node = queue[pos]
        pos += 1
        if values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


def balanced_tree(lo, hi):
    """A perfectly balanced BST holding lo, lo + 1, ..., hi - 1 (built without recursion)."""
    if lo >= hi:
        return None
    root = Node((lo + hi) // 2)
    stack = [(root, lo, hi)]
    while stack:
        node, a, b = stack.pop()
        m = node.value
        if a < m:
            node.left = Node((a + m) // 2)
            stack.append((node.left, a, m))
        if m + 1 < b:
            node.right = Node((m + 1 + b) // 2)
            stack.append((node.right, m + 1, b))
    return root
