class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        h = self.heap
        h.append(value)
        i = len(h) - 1
        while i > 0 and h[i] < h[(i - 1) // 2]:
            p = (i - 1) // 2
            h[i], h[p] = h[p], h[i]
            i = p

    def delete(self):
        h = self.heap
        if not h:
            return None
        top = h[0]
        last = h.pop()
        if h:
            h[0] = last
            i = 0
            while True:
                small = i
                for c in (2 * i + 1, 2 * i + 2):
                    if c < len(h) and h[c] < h[small]:
                        small = c
                if small == i:
                    break
                h[i], h[small] = h[small], h[i]
                i = small
        return top

    def peek(self):
        return self.heap[0] if self.heap else None
