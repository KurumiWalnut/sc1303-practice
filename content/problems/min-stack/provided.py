def run_ops(ops):
    """ops is a list like [("push", 5), ("top",), ("min",), ("pop",)]. Returns what top and min returned."""
    s = MinStack()
    out = []
    for op in ops:
        if op[0] == "push":
            s.push(op[1])
        elif op[0] == "pop":
            s.pop()
        elif op[0] == "top":
            out.append(s.top())
        else:
            out.append(s.get_min())
    return out
