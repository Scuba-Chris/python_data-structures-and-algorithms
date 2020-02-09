class Node:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None
        self.arr = []

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def traversal_action(self, value):
        pass

    def pre_order(self, node=None):
        output = []
        if node == None:
            node = self.root
        output.append(node.value)
        if node._left == None:
            output += self.pre_order(node._left)
        if node._right == None:
            output += self.pre_order(node._right)
        return output
    
    def in_order(self, node=None):
        output = []
        if node == None:
            node = self.root
        if node._left == None:
            output += self.in_order(node._left)
        output.append(node.value)
        if node._right == None:
            output += self.in_order(node._right)
        return output

    def post_order(self, node=None):
        output = []
        if node._left == None:
            output += self.post_order(node._left)
        if node._right == None:
            output += self.post_order(node._right)
        output.append(node.value)
        return output

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def _add(self, value, root=None):
        node = Node(value)
        root = root or self.root
        if self.root == None:
            self.root = node
            return

        if value < root.value:
            if root._left:
                self._add(value, root._left)
            else:
                root._left = node
                return
        else:
            if root._right:
                self._add(value, root._right)
            else:
                root._right = node
                return


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



        

