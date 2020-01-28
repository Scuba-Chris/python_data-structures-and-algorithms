def merge_lists(self, a, b):

    if not a.head:
        a.head = b.head
        return a
    
    current_a = a.head
    current_b = b.head

    while current_a and current_b:
        next_a = current_a.next
        next_b = current_b.next

        current_a.next = current_b
        current_a = next_a

        if next_a:
            current_b.next = next_a
            current_b = next_b
        else:
            break
    
    return a