def find_center(edges):
    a, b = edges[0]
    return a if a in edges[1] else b
