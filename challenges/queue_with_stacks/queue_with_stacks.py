from data_structures/stacks_and_queues/stacks_and_queues.py import Stacks

class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class PseudoQueue:
    def __init__(self):
        self.top = None

    def enqueue(self, value, main_stack=None, helper_stack=None):
        while current_top:
            current_top = main_stack.pop()
            helper_stack.push(current)
        current_top = current_top.next    
        helper_stack.push(value)
        
        while current_top:
            current_top = helper_stack.pop()
            main_stack.push(current_top)
        current_top = current.next_top