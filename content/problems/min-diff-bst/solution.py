def min_diff(root):
    values = []

    def walk(node):                  # in-order: sorted values
        if node is None:
            return
        walk(node.left_child)
        values.append(node.value)
        walk(node.right_child)

    walk(root)
    return min(b - a for a, b in zip(values, values[1:]))
