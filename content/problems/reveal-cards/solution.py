from collections import deque


def deck_revealed_increasing(deck):
    positions = deque(range(len(deck)))
    out = [0] * len(deck)
    for card in sorted(deck):
        out[positions.popleft()] = card        # this position is revealed next
        if positions:
            positions.append(positions.popleft())   # the next one goes to the bottom
    return out
