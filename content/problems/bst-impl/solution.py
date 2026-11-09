def search(search_value, node):
    if node is None or node.value == search_value:
        return node
    if search_value < node.value:
        return search(search_value, node.left_child)
    return search(search_value, node.right_child)


def insert(value, node):
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)
    elif value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)


def max_value(node):
    while node.right_child is not None:    # the largest value is the rightmost node
        node = node.right_child
    return node.value


def min_value(node):
    while node.left_child is not None:     # the smallest value is the leftmost node
        node = node.left_child
    return node.value
