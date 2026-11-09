class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def build_list(values):
    """[1, 2, 3] -> the list 1 -> 2 -> 3. Returns the head (None if values is empty)."""
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def to_pylist(head, limit=1_000_000):
    """The list 1 -> 2 -> 3 -> [1, 2, 3]."""
    out = []
    while head is not None and len(out) < limit:
        out.append(head.data)
        head = head.next
    return out
