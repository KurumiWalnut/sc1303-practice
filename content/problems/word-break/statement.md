Write `word_break(s, word_dict)` that returns `True` if `s` can be split into a sequence of one or more words from `word_dict`. A word can be used any number of times.

### Examples

```text
word_break("leetcode", ["leet", "code"])                         →  True
word_break("applepenapple", ["apple", "pen"])                    →  True
word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])   →  False
```

### Constraints

- `1 <= len(s) <= 300`; up to 1000 words of up to 20 letters.
