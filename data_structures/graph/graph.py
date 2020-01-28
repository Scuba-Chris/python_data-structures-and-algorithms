class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.adjacency_list[v] = []
        return v

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adjacency_list:
            raise KeyError('start vertex is not in the graph')
        if end_vertex not in self.adjacency_list:
            raise KeyError('end vertex is not in the graph')

        adjacencies = self.adjacency_list[start_vertex]

        adjacencies.append((end_vertex, weight))

    def get_node(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

class Vertex:

    def __init__(self, value):
        self.value = value