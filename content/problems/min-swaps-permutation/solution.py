def minimum_swaps(perm):
    seen = [False] * len(perm)
    cycles = 0
    for start in range(len(perm)):
        if not seen[start]:
            cycles += 1
            i = start
            while not seen[i]:                # follow the cycle
                seen[i] = True
                i = perm[i]
    return len(perm) - cycles
