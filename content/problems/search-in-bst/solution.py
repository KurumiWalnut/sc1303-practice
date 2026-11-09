def search_bst(root, val):
    node = root
    while node is not None and node.value != val:
        node = node.left_child if val < node.value else node.right_child
    return node
