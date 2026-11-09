class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.children["*"] = None

    def collect_all_words(self, node=None, word="", words=None):
        if words is None:               # a new list for every top-level call
            words = []
        current = node or self.root
        for key, child in current.children.items():
            if key == "*":
                words.append(word)      # a whole word ends here
            else:
                self.collect_all_words(child, word + key, words)
        return words

    def autocomplete(self, prefix):
        node = self.search(prefix)
        if node is None:
            return []
        return self.collect_all_words(node, prefix)
