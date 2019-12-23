from tree import Node, BinaryTree, BinarySearchTree

def test_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_root():
    tree = BinarySearchTree()
    tree._add(1)
    assert tree.root.value == 1

def test_add():
    tree = BinarySearchTree()
    tree._add(10)
    tree._add(8)
    tree._add(21)

    assert tree.root.value == 10
    assert tree.root._right.value == 21
    assert tree.root._left.value == 8

def test_pre_order():
    tree = BinarySearchTree()
    tree._add(10)
    tree._add(8)
    tree._add(21)

    expected = [10,8,21]
    actual = tree.pre_order()
    assert expected == actual