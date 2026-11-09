def balance_bst(root):
    values = []

    def inorder(node):
        if node is not None:
            inorder(node.left_child)
            values.append(node.value)
            inorder(node.right_child)

    def build(lo, hi):
        if lo >= hi:
            return None
        mid = (lo + hi) // 2
        return TreeNode(values[mid], build(lo, mid), build(mid + 1, hi))

    inorder(root)
    return build(0, len(values))
