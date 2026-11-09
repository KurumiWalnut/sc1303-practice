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
        # TODO: every word below node, each starting with `word`
        pass

    def autocomplete(self, prefix):
        # TODO
        pass
