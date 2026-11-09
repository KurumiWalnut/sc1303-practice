## Collecting every word below a node

To list all the words in a trie, or below some node, walk every path down from that node. Carry the letters seen so far, and record a word whenever you meet a `"*"`:

```python
def collect_all_words(self, node=None, word="", words=None):
    if words is None:              # NOT words=[] in the signature (see below)
        words = []
    current = node or self.root
    for key, child in current.children.items():
        if key == "*":
            words.append(word)      # a complete word ends here
        else:
            self.collect_all_words(child, word + key, words)
    return words
```

This is a depth-first traversal: the trie's version of pre-order.

## Autocomplete

1. Walk down the **prefix** with `search(prefix)`.
2. If the walk fails, there are no suggestions.
3. Otherwise collect every word below that node, **starting the word as the prefix**.

```python
def autocomplete(self, prefix):
    node = self.search(prefix)
    if node is None:
        return []
    return self.collect_all_words(node, prefix, [])
```

The cost is O(length of prefix + size of the part of the trie below it). It doesn't depend on the total number of words, which is why tries power search boxes.

## Ranking suggestions

Real autocomplete returns only the **best few** results:

- **Alphabetical:** `sorted(words)[:3]`, or visit children in sorted key order so words come out alphabetically.
- **Most popular:** store a count at each word's `"*"` node and sort by it.

## The mutable default trap

```python
def collect_all_words(self, node=None, word="", words=[]):   # BUG
```

A default list is created **once**, when the function is defined, and then **shared by every call**. The second autocomplete returns the first call's words too. Use `words=None` and create a new list inside, or always pass a fresh `[]`.

## Counting instead of listing

To answer "how many words start with `pre`?" quickly, keep a `count` on every node and add 1 to each node you pass during `insert`. The answer is then the count on the prefix's last node: O(K), with no collecting.

## Common bugs

- Starting `word` as `""` instead of the prefix, which returns `"t"` instead of `"cat"`.
- Recursing into the `"*"` key (its value is `None`).
- The mutable default list above.
