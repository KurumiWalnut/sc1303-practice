class MapSum:
    def __init__(self):
        self.values = {}                # key -> current value
        self.root = {"#": 0}            # "#" is the total of the keys below this node

    def insert(self, key, val):
        delta = val - self.values.get(key, 0)
        self.values[key] = val
        node = self.root
        node["#"] += delta
        for char in key:
            node = node.setdefault(char, {"#": 0})
            node["#"] += delta

    def sum(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return node["#"]
