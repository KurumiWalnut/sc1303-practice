## Last in, first out

A **stack** is like a pile of plates: you add to the **top** and take from the **top**. The last item pushed is the first one popped (**LIFO**). Only the top item can be read.

| Operation | Meaning | Python list | Cost |
|---|---|---|---|
| push | add to the top | `stack.append(x)` | O(1) |
| pop | remove and return the top | `stack.pop()` | O(1) |
| read / peek | look at the top | `stack[-1]` | O(1) |
| is empty? | | `not stack` | O(1) |

Use the **end** of the list as the top. Pushing and popping at the front (`insert(0, x)`, `pop(0)`) shifts every element: O(N).

```python
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if self.data else None

    def read(self):
        return self.data[-1] if self.data else None
```

## When to reach for a stack

- **Undo:** push each action, and pop to undo the most recent one.
- **Matching pairs:** brackets, tags. Push openers, and pop when the matching closer arrives.
- **Reversing:** push everything, then pop it all.
- **"Cancel the previous item"** (*Remove All Adjacent Duplicates*): compare with the top, and pop if they cancel.
- **Expressions:** in Reverse Polish Notation (`2 1 + 3 *`), push numbers, and for an operator pop two, combine them and push the result. Pop order matters: the **first** pop is the **right**-hand operand.

## Monotonic stack: "next greater element"

*Daily Temperatures* asks, for each day, how long until a warmer day. Keep a stack of **indexes still waiting** for a warmer day. Their temperatures are decreasing from bottom to top. When a warmer day arrives, pop everything colder than it: each popped day's answer is `today - that_day`.

```python
answer = [0] * len(temps)
waiting = []
for i, t in enumerate(temps):
    while waiting and temps[waiting[-1]] < t:
        j = waiting.pop()
        answer[j] = i - j
    waiting.append(i)
```

Each index is pushed and popped once, so it's O(N) despite the nested loop.

## Min stack: extra info per level

To answer "what's the smallest value in the stack?" in O(1), store **the minimum so far** next to each value as you push. Then popping brings back the old minimum automatically.

## Common bugs

- Popping from an empty stack. Check first.
- Swapping the operands of `-` and `/`.
- Truncating division the wrong way: `-7 // 2` is `-4` in Python, but RPN questions want `-3`. Use `int(a / b)`.
