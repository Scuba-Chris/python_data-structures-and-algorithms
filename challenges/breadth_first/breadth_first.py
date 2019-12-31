from data_structures.tree.tree import BinarySearchTree
# from data_structures.stacks_and_queues.stacks_and_queues import Queue
from collections import deque

tree = BinarySearchTree()

def breadth_first(tree):
    if not tree.root:
        return None
    
    new_lst = []
    q = deque()
    q.appendleft(tree.root)
    current = q.pop()

    while len(q):
        q.pop()
        new_lst.append(current.value)
        if current._left:
            q.appendleft(current._left)
        if current._right:
            q.appendleft(current._right)
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

        q = deque()
        q.appendleft(self.root)

        while True:
            current = q.pop()
            if current._left:
                q.appendleft(current._left)
            else:
                current._left = node
                break
            
            if current._right:
                q.appendleft(current._right)
            else:
                current._right = node
                break
