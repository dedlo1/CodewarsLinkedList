class Node(object):
    def __init__(self, next=None):
        self.next = next

def loop_size(node):

    tortoise = node.next
    hare = node.next.next

    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next

    hare = hare.next
    size = 1

    while tortoise != hare:
        hare = hare.next
        size += 1

    return size