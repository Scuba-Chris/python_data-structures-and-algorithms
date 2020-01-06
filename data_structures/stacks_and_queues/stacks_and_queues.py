class Node:
    def __init__(self, value, next=None):
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
        new_top = self.top.next
        self.top = new_top
        return new_top.value

    def peek(self):
        if not self.top:
            raise EmptyStackException('stack empty')
        top_value = self.top.value
        return top_value
    
    def is_empty(self):
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
        if self.front == None:
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if not self.front:
            raise EmptyQueueException('well then')

        removed_node = self.front
        self.front = removed_node.next
        removed_node.next == None
        return removed_node.value

    def peek(self):
        if not self.front:
            raise EmptyQueueException('well then')
        front_value = self.front
        return front_value

    def is_empty(self):
        if not self.front:
            return True
        else:
            return False

class EmptyQueueException(AttributeError):
    pass

class EmptyStackException(AttributeError):
    pass