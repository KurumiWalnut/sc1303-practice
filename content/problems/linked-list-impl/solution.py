def to_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.data)
        current = current.next
    return values


def append(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next is not None:      # walk to the tail
        current = current.next
    current.next = new_node
    return head


def prepend(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node


def delete_value(head, value):
    if head is None:
        return None
    if head.data == value:               # deleting the head
        return head.next
    current = head
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next   # skip over the node
            return head
        current = current.next
    return head


def reversed_values(head):
    stack = []
    current = head
    while current is not None:
        stack.append(current.data)
        current = current.next
    out = []
    while stack:
        out.append(stack.pop())
    return out
