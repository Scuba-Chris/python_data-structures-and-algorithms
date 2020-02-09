from data_structures.graph.graph import Graph, Vertex

def depth_first(self, vertex):
    if vertex not in self.get_node:
        raise ValueError
    visited,output = set(),[]
    def recurese(vertex):
        visited.add(vertex)
        output.append(vertex.value)
        for vert in self.get_node(vertex):
            if vert not in visited:
                recurese(vert)
    recurese(vertex)
    return output