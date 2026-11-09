class WordDictionary:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["*"] = None

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return "*" in node
            char = word[i]
            if char == ".":
                return any(dfs(child, i + 1) for key, child in node.items() if key != "*")
            return char in node and dfs(node[char], i + 1)

        return dfs(self.root, 0)
