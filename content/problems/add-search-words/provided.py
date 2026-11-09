def run_ops(ops):
    '''ops is a list like [("add", "bad"), ("search", ".ad")]. Returns the search results in order.'''
    wd = WordDictionary()
    out = []
    for op, word in ops:
        if op == "add":
            wd.add_word(word)
        else:
            out.append(wd.search(word))
    return out
