class Node:
    def __init__(self, value), next=None:
        self.value = value 
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        # temp = self.top
        new_top = self.top.next
        self.top = new_top
        return new_top.value

    def peek(self):
        top_value = self.top.value
        return top_value
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        new_node.next = self.rear
        self.rear = new_node
        if not self.front:
            self.front = self.rear
    
    def dequeue(self):
        if not self.front:
            raise EmptyQueueException('well then')

        removed_node = self.front
        self.front = removed_node.next
        removed_node.next == None
        return removed_node.value

    def peep(self):
        if not self.front:
            raise EmptyQueueException('well then')
        front_value = self.front
        return front_value

class EmptyQueueException(AttributeError):
            pass