def prefix_count(words, pref):
    root = {"#": 0}                     # "#" holds how many words pass through this node
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, {"#": 0})
            node["#"] += 1
    node = root
    for char in pref:
        if char not in node:
            return 0
        node = node[char]
    return node["#"]
