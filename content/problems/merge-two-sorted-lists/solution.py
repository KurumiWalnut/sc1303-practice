def merge_two_lists(list1, list2):
    dummy = Node(None)           # placeholder in front of the merged list
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 is not None else list2   # attach whatever is left
    return dummy.next
