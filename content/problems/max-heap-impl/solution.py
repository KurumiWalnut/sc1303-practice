class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)                      # new last node
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            p = self._parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]   # trickle up
            i = p

    def delete(self):
        if not self.heap:
            return None
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:                                # more than one element was there
            self.heap[0] = last                      # last node becomes the trickle node
            i, n = 0, len(self.heap)
            while True:
                left, right = self._left(i), self._right(i)
                bigger = i
                if left < n and self.heap[left] > self.heap[bigger]:
                    bigger = left
                if right < n and self.heap[right] > self.heap[bigger]:
                    bigger = right
                if bigger == i:                      # no child is bigger: done
                    break
                self.heap[i], self.heap[bigger] = self.heap[bigger], self.heap[i]
                i = bigger
        return top

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)
