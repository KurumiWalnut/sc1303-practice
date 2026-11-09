class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        node = self.root
        while True:
            if value == node.value:
                return                                   # ignore duplicates
            if value < node.value:
                if node.left_child is None:
                    node.left_child = TreeNode(value)
                    return
                node = node.left_child
            else:
                if node.right_child is None:
                    node.right_child = TreeNode(value)
                    return
                node = node.right_child

    def contains(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left_child if value < node.value else node.right_child
        return False

    def inorder(self):
        out = []

        def walk(node):
            if node is None:
                return
            walk(node.left_child)
            out.append(node.value)
            walk(node.right_child)

        walk(self.root)
        return out

    def range_sum(self, low, high):
        def total(node):
            if node is None:
                return 0
            if node.value < low:
                return total(node.right_child)          # the left side is all too small
            if node.value > high:
                return total(node.left_child)           # the right side is all too big
            return node.value + total(node.left_child) + total(node.right_child)

        return total(self.root)
