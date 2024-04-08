class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    node = head
    node_prev = None
    while node:
        if node_prev and node.data == node_prev.data:
            node_prev.next = node.next
        else:
            node_prev = node
        node = node.next
    return head
