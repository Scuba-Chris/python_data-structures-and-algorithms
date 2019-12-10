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

def test_append(make_list):
    make_list.append(50)
    assert make_list.includes(50)
    assert make_list.to_string( ) == '19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 50 '

def test_insert_before(make_list):
    make_list.insert_before(15,29)
    assert make_list.includes(29)
    assert make_list.to_string() == '19 18 17 16 29 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 '

def test_inser_after(make_list):
    make_list.insert_after(18,31)
    assert make_list.includes(31)
    assert make_list.to_string() == '19 31 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1'

@pytest.fixture()
def make_list():
    test_list = LinkedList()
    for i in range(1, 20):
        test_list.insert(i)
    return test_list