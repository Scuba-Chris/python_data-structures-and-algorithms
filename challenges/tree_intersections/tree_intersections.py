class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def find_intersection(tree_a, tree_b):
    union = set()
    intersection = set()
    root_a = tree_a.root
    root_b = tree_b.root
    if root_a == None or root_b == None:
        return intersection
    walk(root_a, union, intersection)
    walk(root_b, union, intersection)
    return intersection

def walk(root, union, intersection):
    if root.left:
        walk(root.left, union, intersection)
    if root.value in union:
        intersection.add(root.value)
    else:
        union.add(root.value)
    if root.right:
        walk(root.right, union, intersection)