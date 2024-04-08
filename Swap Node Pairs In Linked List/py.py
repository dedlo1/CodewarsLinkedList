class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new_head = head.next
    current = head
    previous = None
    while current is not None and current.next is not None:
        if previous is not None:
            previous.next = current.next
        temp = current.next.next
        current.next.next = current
        current.next = temp
        previous = current
        current = temp
    return new_head