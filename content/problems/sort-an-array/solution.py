import random


def sort_array(nums):
    a = list(nums)

    def qs(low, high):
        while low < high:
            pivot = a[random.randint(low, high)]
            lt, i, gt = low, low, high          # a[low:lt] < pivot, a[gt+1:high+1] > pivot
            while i <= gt:
                if a[i] < pivot:
                    a[lt], a[i] = a[i], a[lt]
                    lt += 1
                    i += 1
                elif a[i] > pivot:
                    a[i], a[gt] = a[gt], a[i]
                    gt -= 1
                else:
                    i += 1
            # Recurse into the smaller side, loop on the bigger one (keeps recursion shallow).
            if lt - low < high - gt:
                qs(low, lt - 1)
                low = gt + 1
            else:
                qs(gt + 1, high)
                high = lt - 1

    qs(0, len(a) - 1)
    return a
