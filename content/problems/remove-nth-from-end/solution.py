def remove_nth_from_end(head, n):
    dummy = Node(None, head)
    fast = slow = dummy
    for _ in range(n):               # put fast n nodes ahead
        fast = fast.next
    while fast.next is not None:     # move both until fast is on the last node
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next       # slow is just before the node to remove
    return dummy.next
