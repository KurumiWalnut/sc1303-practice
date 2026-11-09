class TrieNode:
    def __init__(self):
        self.children = {}      # character -> TrieNode, and "*" -> None at the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None             # the path breaks: not even a prefix
            current = current.children[char]
        return current

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.children["*"] = None    # mark the end of a whole word

    def contains(self, word):
        node = self.search(word)
        return node is not None and "*" in node.children

    def starts_with(self, prefix):
        return self.search(prefix) is not None
