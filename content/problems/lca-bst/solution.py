def lowest_common_ancestor(root, p, q):
    node = root
    while True:
        if p < node.value and q < node.value:
            node = node.left_child
        elif p > node.value and q > node.value:
            node = node.right_child
        else:
            return node.value       # the paths to p and q split here
