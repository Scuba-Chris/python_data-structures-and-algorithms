
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def includes(self, target_node):
        if not self.head:
            return False
        current = self.head

        while current:
            if current.value == target_node:
                return True
            current = current.next
        return False
            