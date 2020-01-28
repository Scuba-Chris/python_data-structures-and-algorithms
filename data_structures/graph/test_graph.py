import pytest
from data_structures.graph.graph import Graph, Vertex

def test_add_node():
    graph = Graph()

    expected = 'fish'
    actual = graph.add_node('fish').value

    assert expected == actual

def test_size():
    graph = Graph()
    graph.add_node('fish')

    expected = 1
    actual = graph.size()

    assert expected == actual

def test_add_edge():
    graph = Graph()
    
    end = graph.add_node('ocean')
    start = graph.add_node('river')

    graph.add_edge(start, end, 21)

    expected = (end, 21)
    actual = graph.adjacency_list[start][0]

    assert expected == actual

def test_get_node():
    graph = Graph()
    graph.add_node('ocean')
    graph.add_node('river')

    expected = 2
    actual = len(graph.get_node())

    assert expected == actual
