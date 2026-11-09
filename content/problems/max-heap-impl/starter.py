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
        """Insert value into the heap."""
        # TODO: Step 1: append value to the end of the array
        # TODO: Step 2: 'trickle up' - compare with parent and swap if larger
        pass

    def delete(self):
        """Delete and return the maximum value (root) from the heap."""
        # TODO: Step 1: handle the empty heap and the single element case
        # TODO: Step 2: move the last element to the root
        # TODO: Step 3: 'trickle down' - swap with the larger child until the heap property holds
        pass

    def peek(self):
        """Return the maximum value without removing it."""
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)
