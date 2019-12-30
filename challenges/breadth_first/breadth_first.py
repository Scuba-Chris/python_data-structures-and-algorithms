from data_structures.tree.tree import BinarySearchTree
from data_structures.stacks_and_queues.stacks_and_queues import Queue

tree = BinarySearchTree()

def breadth_first(tree):
    if not tree.root:
        return None
    
    new_lst = []
    q = Queue()
    q.enqueue(tree.root)
    current = q.dequeue()

    while len(q):
        q.dequeue()
        new_lst.append(current.value)
        if current._left:
            q.enqueue(current._left)
        if current._right:
            q.enqueue(current._right)
    return new_lst

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        q = Queue()
        q.enqueue(self.root)

        while True:
            current = q.dequeue()
            if current._left:
                q.enqueue(current._left)
            else:
                current._left = node
                break
            
            if current._right:
                q.enqueue(current._right)
            else:
                current._right = node
                break
