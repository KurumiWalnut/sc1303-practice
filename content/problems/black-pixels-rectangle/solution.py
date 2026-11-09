def min_area(image, x, y):
    m, n = len(image), len(image[0])

    def row_has_black(r):
        return any(image[r][c] == "1" for c in range(n))

    def col_has_black(c):
        return any(image[r][c] == "1" for r in range(m))

    def first_true(low, high, check):     # smallest i in low..high with check(i); check(high) is True
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low

    def last_true(low, high, check):      # largest i in low..high with check(i); check(low) is True
        while low < high:
            mid = (low + high + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid - 1
        return low

    top = first_true(0, x, row_has_black)
    bottom = last_true(x, m - 1, row_has_black)
    left = first_true(0, y, col_has_black)
    right = last_true(y, n - 1, col_has_black)
    return (bottom - top + 1) * (right - left + 1)
