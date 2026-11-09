class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if self.data else None

    def read(self):
        return self.data[-1] if self.data else None

    def is_empty(self):
        return not self.data

    def __len__(self):
        return len(self.data)


def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    out = []
    while not stack.is_empty():
        out.append(stack.pop())
    return "".join(out)
