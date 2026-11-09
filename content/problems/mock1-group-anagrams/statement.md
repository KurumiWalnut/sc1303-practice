Write `group_anagrams(words)` that groups the words that are **anagrams** of each other: words made of exactly the same letters, the same number of times (for example `"eat"`, `"tea"` and `"ate"`).

Return a list of groups, where each group is a list of words. The groups and the words inside each group can be in **any order**. Every input word appears exactly once in the output, so repeated words go in the same group.

### Examples

```text
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    →  [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

group_anagrams([""])   →  [[""]]
group_anagrams(["a"])  →  [["a"]]
```

### Constraints

- `1 ≤ len(words) ≤ 20 000`
- Each word has at most 100 lowercase letters.
