from breadth_first import breadth_first, BinaryTree, Node
from data_structures.stacks_and_queues.stacks_and_queues import Queue
import pytest

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_add_root():
    tree = BinaryTree()
    tree.add(5)
    
    assert tree.root.value == 5

def test_add():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(6)
    tree.add(8)
    tree.add(2)
    # breakpoint()
    tree.add(1)

    assert tree.root.value == 5
    assert tree.root._left.value == 3
    assert tree.root._right.value == 6
    assert tree.root._left._left.value == 8
    assert tree.root._left._right.value == 2
    assert tree.root._right._left.value == 1
    


@pytest.mark.skip('pending')
def test_breadth_first():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(6)
    tree.add(8)
    tree.add(2)
    tree.add(1)
