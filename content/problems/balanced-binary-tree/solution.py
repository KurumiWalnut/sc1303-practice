def is_balanced(root):
    def check(node):
        # Height of the subtree, or -1 if it's unbalanced somewhere.
        if node is None:
            return 0
        left = check(node.left_child)
        if left < 0:
            return -1
        right = check(node.right_child)
        if right < 0 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) >= 0
