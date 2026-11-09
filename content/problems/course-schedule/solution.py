from collections import deque


def can_finish(num_courses, prerequisites):
    after = [[] for _ in range(num_courses)]       # b -> courses that need b
    indeg = [0] * num_courses
    for a, b in prerequisites:
        after[b].append(a)
        indeg[a] += 1
    queue = deque(c for c in range(num_courses) if indeg[c] == 0)
    taken = 0
    while queue:
        c = queue.popleft()
        taken += 1
        for nxt in after[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses
