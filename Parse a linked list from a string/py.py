class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if not s:
        return
    s = s.split(' -> ')
    head = Node(s[0])
    current = head
    for i in range(1, len(s)):
        current.next = Node(s[i])
        current = current.next
    return head