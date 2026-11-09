def run_ops(ops):
    '''ops is a list like [("insert", "apple", 3), ("sum", "ap")]. Returns the sum results in order.'''
    m = MapSum()
    out = []
    for op in ops:
        if op[0] == "insert":
            m.insert(op[1], op[2])
        else:
            out.append(m.sum(op[1]))
    return out
