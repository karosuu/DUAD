class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head = Node | None

    def __init__(self, head):
        self.head = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self, node):
        current_node = self.head
        
        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = node

    def dequeue(self):
        if self.head:
            self.head = self.head.next


first_node = Node("A")

second_node = Node("B")
first_node.next = second_node

third_node = Node("C")
second_node.next = third_node

structure = Queue(first_node)
structure.print_structure()