def quick_sort_trace(arr):
    trace = []

    def partition(low, high):
        pivot = arr[high]
        b = low
        for a in range(low, high):
            if arr[a] < pivot:
                arr[a], arr[b] = arr[b], arr[a]
                b += 1
        arr[b], arr[high] = arr[high], arr[b]
        return b

    def qs(low, high):
        if low < high:
            p = partition(low, high)
            trace.append(p)
            qs(low, p - 1)
            qs(p + 1, high)

    qs(0, len(arr) - 1)
    return trace
