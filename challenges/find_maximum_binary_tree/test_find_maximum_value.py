from challenges.find_maximum_binary_tree.find_Maximum_value import Node, return_max
from challenges.breadth_first.breadth_first import BinaryTree
import pytest

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

