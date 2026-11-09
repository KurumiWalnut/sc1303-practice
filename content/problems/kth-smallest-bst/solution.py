def kth_smallest(root, k):
    stack, node = [], root
    while True:
        while node is not None:          # go as far left as possible
            stack.append(node)
            node = node.left_child
        node = stack.pop()               # next value in sorted order
        k -= 1
        if k == 0:
            return node.value
        node = node.right_child
