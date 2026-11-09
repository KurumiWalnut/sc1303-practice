class TrieNode:
    def __init__(self):
        self.children = {}      # character -> TrieNode, and "*" -> None at the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        # TODO: return the node after the last character, or None
        pass

    def insert(self, word):
        # TODO: remember the "*" end marker
        pass

    def contains(self, word):
        # TODO
        pass

    def starts_with(self, prefix):
        # TODO
        pass
