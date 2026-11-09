def run_ops(ops):
    """ops is a list like [("add", 1), ("add", 2), ("median",)]. Returns the medians, in order."""
    finder = MedianFinder()
    out = []
    for op in ops:
        if op[0] == "add":
            finder.add_num(op[1])
        else:
            out.append(finder.find_median())
    return out
