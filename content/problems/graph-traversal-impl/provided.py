class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)


def build_graph(adjacency):
    """Turn {"A": ["B", "C"], ...} into Vertex objects. Returns {value: Vertex}."""
    vertices = {}
    for value, neighbours in adjacency.items():
        for v in [value, *neighbours]:
            if v not in vertices:
                vertices[v] = Vertex(v)
    for value, neighbours in adjacency.items():
        for n in neighbours:
            vertices[value].add_adjacent_vertex(vertices[n])
    return vertices
