def bst_from_preorder(preorder):
    index = 0

    def build(high):
        nonlocal index
        if index == len(preorder) or preorder[index] > high:
            return None
        node = TreeNode(preorder[index])
        index += 1
        node.left_child = build(node.value)      # left subtree: values below node
        node.right_child = build(high)           # right subtree: up to the parent's bound
        return node

    return build(float("inf"))
