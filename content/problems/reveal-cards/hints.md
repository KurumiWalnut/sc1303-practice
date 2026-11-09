Simulate the process on **positions** instead of cards.

---

Put the indexes `0 … n-1` in a `deque`. Then, for each card in sorted order: the front index gets that card (`popleft`), and the next front index moves to the back (`append(popleft())`).
