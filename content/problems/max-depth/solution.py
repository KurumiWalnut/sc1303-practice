def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left_child), max_depth(root.right_child))
