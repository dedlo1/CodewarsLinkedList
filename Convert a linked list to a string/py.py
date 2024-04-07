class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if node is None:
        return "None"
    return f"{node.data} -> {stringify(node.next)}"

assert stringify(Node(1, Node(2, Node(3)))) == "1 -> 2 -> 3 -> None"
