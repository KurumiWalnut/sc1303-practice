def delete(root, value):
    if root is None:
        return None                               # not found
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right                     # zero or one child
        if root.right is None:
            return root.left
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.value = successor.value
        root.right = delete(root.right, successor.value)

    _update_height(root)
    balance = _get_balance(root)
    if balance < -1:
        if _get_balance(root.left) <= 0:
            return _rotate_right(root)            # LL
        root.left = _rotate_left(root.left)       # LR
        return _rotate_right(root)
    if balance > 1:
        if _get_balance(root.right) >= 0:
            return _rotate_left(root)             # RR
        root.right = _rotate_right(root.right)    # RL
        return _rotate_left(root)
    return root
