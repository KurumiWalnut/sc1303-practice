def find_judge(n, trust):
    indeg = [0] * (n + 1)
    outdeg = [0] * (n + 1)
    for a, b in trust:
        outdeg[a] += 1
        indeg[b] += 1
    for person in range(1, n + 1):
        if outdeg[person] == 0 and indeg[person] == n - 1:
            return person
    return -1
