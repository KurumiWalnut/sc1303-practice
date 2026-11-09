def trim_bst(root, low, high):
    if root is None:
        return None
    if root.value < low:                       # root and its left side are too small
        return trim_bst(root.right_child, low, high)
    if root.value > high:                      # root and its right side are too big
        return trim_bst(root.left_child, low, high)
    root.left_child = trim_bst(root.left_child, low, high)
    root.right_child = trim_bst(root.right_child, low, high)
    return root
