class Node:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def pre_order(self, node=None):
        output = []
        if node == None:
            node = self.root
        output.append(node.value)
        if node._left != None:
            output += self.pre_order(node._left)
        if node._right != None:
            output += self.pre_order(node._right)
        return output
    
    def in_order(self, node=None):
        output = []
        if node == None:
            node = self.root
        if node._left == None:
            output += self.pre_order(node._left)
        output.append(node.value)
        if node._right == None:
            output += self.pre_order(node._right)
        return output

    def post_order(self, node=None):
        output = []
        if node._left == None:
            output += self.pre_order(node._left)
        if node._right == None:
            output += self.pre_order(node._right)
        output.append(node.value)
        return output

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def _add(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value > current.value:
                if not current._right:
                    current._right = Node(value)
                    return
                else:
                    current = current._right
            else:
                if not current._left:
                    current._left = Node(value)
                    return
                else:
                    current = current._left

    def contains(self, value):
        _contains = []
        if self.root == None:
            return False
        current = self.root
        if value == current.value:
            return True
        elif value < current.value:
            if current._left == value:
                return True
    

                


class EmptyTree(ValueError):
    pass



        

