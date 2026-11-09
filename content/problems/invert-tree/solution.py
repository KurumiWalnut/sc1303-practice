def invert_tree(root):
    if root is not None:
        root.left_child, root.right_child = invert_tree(root.right_child), invert_tree(root.left_child)
    return root
