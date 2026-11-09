The starter code has the trie from the last subtopic, with `insert` and `search` done. Add two methods:

- **`collect_all_words(node=None, word="", words=None)`**: return a list of every word stored **below** `node` (the root if `node` is `None`). `word` is the text spelled so far, and is put in front of everything found. Recurse into each child with `word + char`, and add `word` to the list when you meet `"*"`.
- **`autocomplete(prefix)`**: return every stored word that starts with `prefix` (including `prefix` itself if it's a word), or `[]` if there are none. Search for the prefix's node, then collect from there, **starting `word` at the prefix**.

The order of the list doesn't matter: the tests sort it.

Watch out for the **mutable default** trap: `words=[]` in the signature is shared by every call.

### Example

```text
words: get, go, got, gotten, hall, ham, hammer, hill, zebra

t.autocomplete("ha")                        →  ['hall', 'ham', 'hammer']
t.autocomplete("go")                        →  ['go', 'got', 'gotten']
t.autocomplete("x")                         →  []
t.collect_all_words(t.search("ham"), "ham") →  ['ham', 'hammer']
t.collect_all_words(t.search("ham"))        →  ['', 'mer']
```
