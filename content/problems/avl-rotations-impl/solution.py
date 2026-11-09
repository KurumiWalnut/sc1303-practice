def _rotate_left(x):
    y = x.right
    t2 = y.left
    y.left = x            # x drops down to y's left
    x.right = t2          # y's old left subtree moves under x
    _update_height(x)     # x first: it's now below y
    _update_height(y)
    return y


def _rotate_right(y):
    x = y.left
    t2 = x.right
    x.right = y           # y drops down to x's right
    y.left = t2           # x's old right subtree moves under y
    _update_height(y)     # y first: it's now below x
    _update_height(x)
    return x
