def insertion_sort_list(head):
    dummy = Node(None)
    tail = dummy                                  # last node of the sorted part
    node = head
    while node is not None:
        nxt = node.next
        if tail is not dummy and tail.data <= node.data:
            tail.next = node                      # belongs at the end: O(1)
            tail = node
            node.next = None
        else:
            prev = dummy
            while prev.next is not None and prev.next.data <= node.data:
                prev = prev.next
            node.next = prev.next                 # splice in after prev
            prev.next = node
            if node.next is None:
                tail = node
        node = nxt
    return dummy.next
