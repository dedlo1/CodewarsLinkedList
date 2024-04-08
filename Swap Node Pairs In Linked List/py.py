class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    # Your code goes here.
    # Remember to return the head of the list.
    current = head
    while current is not None:
        if current.next is not None:
            current, current.next = current.next, current
        current = current.next
    return head
