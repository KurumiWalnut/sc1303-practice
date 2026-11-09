def add_two_numbers(l1, l2):
    dummy = Node(None)
    tail = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry:
        total = carry
        if l1 is not None:
            total += l1.data
            l1 = l1.next
        if l2 is not None:
            total += l2.data
            l2 = l2.next
        carry, digit = divmod(total, 10)
        tail.next = Node(digit)
        tail = tail.next
    return dummy.next
