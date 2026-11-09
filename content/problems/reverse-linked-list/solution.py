def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        following = current.next     # save the rest of the list
        current.next = previous      # flip the link
        previous = current
        current = following
    return previous
