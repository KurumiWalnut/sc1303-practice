def run_ops(ops):
    """ops is a list like [("push", 1), ("peek",), ("pop",), ("empty",)]. Returns what pop, peek and empty returned."""
    q = MyQueue()
    out = []
    for op in ops:
        if op[0] == "push":
            q.push(op[1])
        elif op[0] == "pop":
            out.append(q.pop())
        elif op[0] == "peek":
            out.append(q.peek())
        else:
            out.append(q.empty())
    return out
