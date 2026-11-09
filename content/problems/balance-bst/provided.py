class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right


def build_tree(values):
    """Level-order list -> tree. None marks a missing child, e.g. [5, 1, 4, None, None, 3, 6]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue, i, pos = [root], 1, 0
    while i < len(values):
        node = queue[pos]
        pos += 1
        if values[i] is not None:
            node.left_child = TreeNode(values[i])
            queue.append(node.left_child)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right_child = TreeNode(values[i])
            queue.append(node.right_child)
        i += 1
    return root


def tree_to_list(root):
    """Tree -> level-order list with None for gaps (the format build_tree takes)."""
    out, queue, pos = [], [root], 0
    while pos < len(queue):
        node = queue[pos]
        pos += 1
        if node is None:
            out.append(None)
            continue
        out.append(node.value)
        queue.append(node.left_child)
        queue.append(node.right_child)
    while out and out[-1] is None:
        out.pop()
    return out


def build_bst(values):
    """Insert values one at a time into an empty BST. Returns the root."""
    root = None
    for v in values:
        if root is None:
            root = TreeNode(v)
            continue
        node = root
        while v != node.value:
            side = "left_child" if v < node.value else "right_child"
            child = getattr(node, side)
            if child is None:
                setattr(node, side, TreeNode(v))
                break
            node = child
    return root


def inorder_values(root):
    """Values in in-order (sorted order for a valid BST), without recursion."""
    out, stack, node = [], [], root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left_child
        node = stack.pop()
        out.append(node.value)
        node = node.right_child
    return out


def check_balanced_bst(root, values):
    """Return "ok" if root is a height-balanced BST holding exactly `values` (sorted); otherwise say what's wrong."""
    got = inorder_values(root) if root is not None else []
    if got != list(values):
        return f"the in-order traversal is {got[:8]}{' ...' if len(got) > 8 else ''}, but it should be {list(values)[:8]}{' ...' if len(values) > 8 else ''}"
    heights = {}
    stack = [(root, False)] if root is not None else []
    while stack:
        node, children_done = stack.pop()
        if children_done:
            hl = heights[id(node.left_child)] if node.left_child else 0
            hr = heights[id(node.right_child)] if node.right_child else 0
            if abs(hl - hr) > 1:
                return f"not balanced at {node.value}: its left subtree has height {hl} and its right subtree has height {hr}"
            heights[id(node)] = 1 + max(hl, hr)
        else:
            stack.append((node, True))
            for child in (node.left_child, node.right_child):
                if child is not None:
                    stack.append((child, False))
    return "ok"
