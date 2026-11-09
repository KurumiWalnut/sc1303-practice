def num_decodings(s):
    n = len(s)
    ways = [0] * (n + 1)
    ways[n] = 1                                   # empty suffix: one way
    for i in range(n - 1, -1, -1):
        if s[i] != "0":
            ways[i] = ways[i + 1]
            if i + 1 < n and "10" <= s[i:i + 2] <= "26":
                ways[i] += ways[i + 2]
    return ways[0]
