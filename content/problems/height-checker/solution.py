def height_checker(heights):
    counts = [0] * 101                         # counting sort: heights are 1..100
    for h in heights:
        counts[h] += 1
    expected = []
    for h in range(101):
        expected += [h] * counts[h]
    return sum(1 for a, b in zip(heights, expected) if a != b)
