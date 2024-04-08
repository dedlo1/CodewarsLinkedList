class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def func(node, prev):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return func(next, node)
    return func(head, None)
     