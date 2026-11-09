class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        node = Node(value)
        if self.tail is None:              # empty: node is both ends
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        if self.head is None:              # list is now empty
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return node.data

    def pop_back(self):
        if self.tail is None:
            return None
        node = self.tail
        self.tail = node.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return node.data

    def to_list(self):
        out, current = [], self.head
        while current is not None:
            out.append(current.data)
            current = current.next
        return out

    def to_list_reversed(self):
        out, current = [], self.tail
        while current is not None:
            out.append(current.data)
            current = current.prev
        return out

    def __len__(self):
        return self.size
