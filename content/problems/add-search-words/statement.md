The tests drive your class through `run_ops` (see **Provided code**), which creates one object, runs the operations in order and returns what the query operations returned.

Write a class `WordDictionary` with:

- **`add_word(word)`**: store a lowercase word.
- **`search(word)`**: return `True` if a stored word **matches** `word`, where a `.` matches **any one** letter. The lengths must match too.

### Example

```text
add_word("bad"), add_word("dad"), add_word("mad")
search("pad")  →  False
search("bad")  →  True
search(".ad")  →  True
search("b..")  →  True
search("b.")   →  False   (too short)
```

### Constraints

- Up to 30 000 calls in total; words have at most 12 letters.
- A search word has at most 2 dots.
