from challenges.tree_intersections.tree_intersections import find_intersection, walk, Node, BinaryTree
from data_structures.tree.tree import BinarySearchTree
import pytest

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None

def test_find_intersection():
    tree_a = BinarySearchTree()
    tree_b = BinarySearchTree()

    tree_a._add(14)
    tree_a._add(13)
    tree_a._add(18)
    tree_a._add(3)

    tree_b._add(14)
    tree_b._add(11)
    tree_b._add(18)
    tree_b._add(3)

    expected = [18, 14, 3]
    actual = find_intersection(tree_a, tree_b)
    assert expected == actual


