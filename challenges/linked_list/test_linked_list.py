import pytest
from linked_list import Node, LinkedList

def test_node_one():
    test_node = Node('value')
    assert isinstance(test_node, Node) 

def test_node_two():
    test_linked_list = LinkedList()
    assert isinstance(test_linked_list, LinkedList)

def test_insert():
    test_list = LinkedList()
    test_list.insert(5)
    assert test_list.head.value == 5
    test_list.insert(3)
    assert test_list.head.value == 3
    assert test_list.head.next.value == 5

def test_includes(make_list):
    assert make_list.includes(5)
    assert not make_list.includes(50)

@pytest.fixture()
def make_list():
    test_list = LinkedList()
    for i in range(21, 1, -1):
        test_list.insert(i)
    return test_list