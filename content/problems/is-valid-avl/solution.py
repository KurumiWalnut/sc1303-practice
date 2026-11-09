def is_valid_avl(root):
    def check(node, low, high):
        # Height of the subtree, or -1 if it breaks a rule.
        if node is None:
            return 0
        if not (low < node.value < high):
            return -1
        left = check(node.left, low, node.value)
        if left < 0:
            return -1
        right = check(node.right, node.value, high)
        if right < 0 or abs(right - left) > 1:
            return -1
        return 1 + max(left, right)

    return check(root, float("-inf"), float("inf")) >= 0
