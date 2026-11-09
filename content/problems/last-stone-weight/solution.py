import heapq


def last_stone_weight(stones):
    heap = [-s for s in stones]          # negatives turn heapq's min-heap into a max-heap
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)         # heaviest
        x = -heapq.heappop(heap)         # second heaviest
        if y != x:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0
