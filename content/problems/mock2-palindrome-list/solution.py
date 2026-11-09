def is_palindrome(head):
    values = []
    while head is not None:
        values.append(head.data)
        head = head.next
    return values == values[::-1]
