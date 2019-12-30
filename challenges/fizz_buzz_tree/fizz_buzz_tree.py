from data_structures.tree.tree import BinaryTree, BinarySearchTree, Node

def fizz_buzz(value):
    adjusted_val = ''

    if value % 3 == 0:
        adjusted_val += 'Fizz'

    if value % 5 == 0:
        adjusted_val += 'Buzz'

    return adjusted_val or str(value)

    # if value % 5 == 0 and value % 3 == 0:
    #     return 'FizzBuzz'
    # elif value % 5 == 0:
    #     return 'Buzz'
    # elif value % 3 == 0:
    #     return 'Fizz'
    # else:
    #     return str(value)

def fizz_buzz_node(node):
    new_node = Node(node.value)
    if node._left:
        new_node._left = fizz_buzz_node(node._left)
    if node._right:
        new_node._right = fizz_buzz_node(node._right)
    new_node.value = fizz_buzz(new_node.value)
    return new_node

def fizz_buzz_tree(tree):
    if not tree.root:
        return None
    node = fizz_buzz_node(tree.root)
    new_tree = BinaryTree(node)
    return new_tree


if __name__ == "__main__":
  
    tree = BinarySearchTree()
    tree._add(10)
    tree._add(8)
    tree._add(21)
    tree._add(41)
    fizz_buzz_tree(tree)