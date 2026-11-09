## What a trie is

A **trie** (pronounced "try") stores words by their letters. Each path from the root spells out the start of one or more words, and words that share a prefix share the same path. That makes prefix questions fast: "is there a word starting with `cat`?" takes 3 steps, however many words are stored.

A trie isn't a binary tree: a node can have **any number** of children. Each node holds a **hash table** (dict) mapping a character to the child node.

```python
class TrieNode:
    def __init__(self):
        self.children = {}          # character -> TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
```

## The `"*"` end marker

How do you know `"bat"` is a word if `"batter"` is stored too? The course puts a `"*"` key in the node after a word's last letter:

```text
root ─ b ─ a ─ t ─┬─ *            "bat" is a word
                  └─ t ─ e ─ r ─ *    and so is "batter"
```

In code: `node.children["*"] = None`.

## Search (walk the prefix)

```python
def search(self, word):
    """Return the node reached after the last character, or None."""
    current = self.root
    for char in word:
        if char in current.children:
            current = current.children[char]
        else:
            return None                 # path breaks: not even a prefix
    return current
```

- **Is it a prefix?** `search(prefix) is not None`
- **Is it a whole word?** the node exists **and** has `"*"` in its children.

## Insert

```python
def insert(self, word):
    current = self.root
    for char in word:
        if char not in current.children:
            current.children[char] = TrieNode()    # create the missing step
        current = current.children[char]
    current.children["*"] = None                   # mark the end of the word
```

## Cost

| Operation | Trie | List of N words | Set of N words |
|---|---|---|---|
| Insert word of length K | **O(K)** | O(1) append | O(K) |
| Is it a word? | **O(K)** | O(N·K) | O(K) |
| Any word with this prefix? | **O(K)** | O(N·K) | O(N·K) |
| All words with this prefix | **O(K + size of answer)** | O(N·K) | O(N·K) |

The trade-off is **memory**: one node per character, each with its own dict.

## Wildcard search

To support `.` meaning "any letter", search recursively: at a `.`, try **every** child. This is DFS on the trie.

## Common bugs

- Forgetting the `"*"` marker, so `"ca"` looks like a word because `"cat"` is stored.
- Treating `"*"` as a letter when looping over children (skip it).
- Writing `if current.children.get(char):` and then storing `None` or a falsy value somewhere. Prefer `char in current.children`.
