class Node:
    def __init__(self, value):
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
        temp = self.top
        new_top = self.top.next
        self.top = new_top
        return new_top.value

    def peek(self):
        top_value = self.top.value
        return top_value
    
    def isEmpty(self):
        if self.top == null:
            return True
        else:
            return False

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        self.rear.next = new_node
        self.rear = new_node
    
    def Dequeue(self):
        temp = self.front
        self.front.next = front
        temp.next == null

    def peep(self):
        front_value = self.front
        return front_value