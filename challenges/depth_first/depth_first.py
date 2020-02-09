from data_structures.graph.graph import Graph, Vertex

def depth_first(self, vertex):
    if vertex not in self.get_node:
        raise ValueError
    visited,output = set(),[]
    def recurse(vertex):
        visited.add(vertex)
        output.append(vertex.value)
        for vert in self.get_node(vertex):
            if vert not in visited:
                recurse(vert)
    recurse(vertex)
    return output