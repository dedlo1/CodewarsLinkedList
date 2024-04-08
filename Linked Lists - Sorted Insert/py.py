""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None:
        return Node(data)
    if data < head.data:
        new_head = Node(data)
        new_head.next = head
        return new_head
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node
    return head
