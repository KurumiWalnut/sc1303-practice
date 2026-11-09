from collections import deque


def first_uniq_char(s):
    counts = {}
    queue = deque()
    for i, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        if counts[ch] == 1:
            queue.append((ch, i))
        while queue and counts[queue[0][0]] > 1:
            queue.popleft()                # the front repeats now: it can never be the answer
    return queue[0][1] if queue else -1
