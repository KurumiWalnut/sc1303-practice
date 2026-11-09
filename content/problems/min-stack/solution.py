class MinStack:
    def __init__(self):
        self.data = []                     # (value, smallest value at or below this level)

    def push(self, val):
        smallest = min(val, self.data[-1][1]) if self.data else val
        self.data.append((val, smallest))

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1][0]

    def get_min(self):
        return self.data[-1][1]
