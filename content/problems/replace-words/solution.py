def replace_words(dictionary, sentence):
    root = {}
    for word in dictionary:
        node = root
        for char in word:
            node = node.setdefault(char, {})
        node["*"] = None

    out = []
    for word in sentence.split():
        node, replacement = root, word
        for i, char in enumerate(word):
            if char not in node:
                break                       # no root fits
            node = node[char]
            if "*" in node:
                replacement = word[:i + 1]  # the first root found is the shortest
                break
        out.append(replacement)
    return " ".join(out)
