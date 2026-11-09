def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    return height(node.right) - height(node.left)


def is_balanced(root):
    # One post-order pass: returns the height, or -1 as soon as something is unbalanced.
    def check(node):
        if node is None:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left < 0 or right < 0 or abs(right - left) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) >= 0


def imbalance_case(node):
    bf = balance_factor(node)
    if bf <= -2:
        return "LL" if balance_factor(node.left) <= 0 else "LR"
    if bf >= 2:
        return "RR" if balance_factor(node.right) >= 0 else "RL"
    return None
