from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft() if self.data else None

    def read(self):
        return self.data[0] if self.data else None

    def is_empty(self):
        return not self.data

    def __len__(self):
        return len(self.data)
