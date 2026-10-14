class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def queue(self, node):
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next
            
        current_node.next = node

    def dequeue(self):
        if self.head:
            self.head = self.head.next


first_node = Node("Hola mundo")
second_node = Node("Soy el segundo nodo")
first_node.next = second_node

third_node = Node("Soy el tercer nodo")
second_node.next = third_node

structure = Queue(first_node)

fourth_node = Node("Soy el nuevo")

structure.queue(fourth_node)

print("Agregando un nodo:")
structure.print_structure()

# structure.print_structure()

# print("DEQUEUE")

# structure.dequeue()

# structure.print_structure()
