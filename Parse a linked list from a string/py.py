class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if not s:
        return
    s = s.split(' -> ')
    head = Node(int(s[0])) if s[0] != 'None' else None
    current = head
    for i in range(1, len(s)):
        current.next = Node(int(s[i])) if i != len(s) - 1 else None
        current = current.next
    return head