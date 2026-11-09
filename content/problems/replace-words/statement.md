A **root** is a short word that other words can be built from: `"cat"` is the root of `"cattle"`.

Write `replace_words(dictionary, sentence)`. Replace every word in `sentence` with the **shortest** root from `dictionary` that it starts with, or leave the word alone if no root fits. Return the new sentence (words are separated by single spaces).

### Examples

```text
replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery")
    →  "the cat was rat by the bat"

replace_words(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs")
    →  "a a b c"
```

### Constraints

- Up to 20 000 roots and 20 000 words.
- Words and roots are lowercase letters only.
