from data_structures.tree.tree import BinarySearchTree, Node
from fizz_buzz_tree import fizz_buzz_tree

def test_fizz_buzz():
    tree = BinarySearchTree()
    tree._add(17)
    tree._add(11)
    tree._add(21)
    tree._add(3)
    tree._add(15)
    tree._add(25)
    tree = fizz_buzz_tree(tree)

    assert tree.root.value == '17'
    assert tree.root._left.value == '11'
    assert tree.root._left._left.value == 'Fizz'
    assert tree.root._left._right.value == 'FizzBuzz'
    assert tree.root._right.value == 'Fizz'
    assert tree.root._right._right.value == 'Buzz'