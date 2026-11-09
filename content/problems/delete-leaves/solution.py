def remove_leaf_nodes(root, target):
    if root is None:
        return None
    root.left_child = remove_leaf_nodes(root.left_child, target)    # children first
    root.right_child = remove_leaf_nodes(root.right_child, target)
    if root.left_child is None and root.right_child is None and root.value == target:
        return None                                                  # now a target leaf
    return root
