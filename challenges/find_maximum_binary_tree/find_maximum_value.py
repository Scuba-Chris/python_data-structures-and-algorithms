from collections import deque
from challenges.breadth_first.breadth_first import BinaryTree

tree = BinaryTree()

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def return_max(tree):
    if not tree.root:
        return None

    q = deque()
    q.appendleft(tree.root)
    current = q.pop()
    largest_value = tree.root.value
    while len(q):
        current = q.pop()
        if current.value > largest_value:
            largest_value = current.value
        if current.left:
            q.appendleft(current.left)
        if current.right:
            q.appendleft(current.right)
    return largest_value
