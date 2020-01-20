
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_string(self):
        results = ''
        Node = self.head
        while Node:
            results += str(Node.value) + ' '
            Node = Node.next
        return results

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
            
    def append(self, value):
        current = self.head
        if current == None:
            self.head = Node(value)
        else:
            while current.next:
                current = current.next
            new_node = Node(value)
            current.next = new_node

    def insert_before(self, value, new_value):
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def kth_from_end(self, k):
        count = 0
        current = self.head
        while current.next:
            current = current.next
            count += 1
        current = self.head
        if k > count:
            return 'Exception'
        for _ in range(count - k):
            current = current.next
        return current.value

