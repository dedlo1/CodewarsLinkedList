class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        current = current.next
    return head
