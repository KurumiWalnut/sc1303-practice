def inorder(node):
    if node is None:
        return []
    return inorder(node.left_child) + [node.value] + inorder(node.right_child)


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left_child) + preorder(node.right_child)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left_child) + postorder(node.right_child) + [node.value]


def is_valid_bst(node, low=None, high=None):
    if node is None:
        return True
    if (low is not None and node.value <= low) or (high is not None and node.value >= high):
        return False
    return (is_valid_bst(node.left_child, low, node.value)
            and is_valid_bst(node.right_child, node.value, high))
