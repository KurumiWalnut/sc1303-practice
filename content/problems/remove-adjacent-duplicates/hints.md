Use a stack of letters.

---

For each letter: if it matches the top of the stack, **pop** (the pair cancels); otherwise **push** it. What's left on the stack, bottom to top, is the answer.

Searching the string for pairs again and again is O(N²) when pairs are nested deep, like `"abccba"`.
