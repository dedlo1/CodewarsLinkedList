class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None or head.next is None:
        raise ValueError
    first = head
    second = head.next
    current = head.next.next
    first_current = first
    second_current = second
    while current is not None:
        first_current.next = current
        first_current = first_current.next
        current = current.next
        if current is None:
            break
        second_current.next = current
        second_current = second_current.next
        current = current.next
    first_current.next = None
    second_current.next = None
    return Context(first, second)