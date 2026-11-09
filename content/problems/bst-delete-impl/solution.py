def delete(value, node):
    if node is None:
        return None
    if value < node.value:
        node.left_child = delete(value, node.left_child)
        return node
    if value > node.value:
        node.right_child = delete(value, node.right_child)
        return node
    if node.left_child is None:              # no children, or only a right child
        return node.right_child
    if node.right_child is None:             # only a left child
        return node.left_child
    node.right_child = lift(node.right_child, node)   # two children
    return node


def lift(node, node_to_delete):
    # Find the successor (leftmost node of this subtree), move its value up,
    # and let its right child take its place.
    if node.left_child is not None:
        node.left_child = lift(node.left_child, node_to_delete)
        return node
    node_to_delete.value = node.value
    return node.right_child
