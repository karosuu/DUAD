class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, node):
        current_node = node
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            previous_head = self.head.data
            self.head = self.head.next

            return previous_head


first_node = Node("Hola")
second_node = Node("Mundo")
first_node.next = second_node
third_node = Node("Python")
second_node.next = third_node
fourth_node = Node("New")

structure = Stack(first_node)
structure.push(fourth_node)

print("\nElemento agregado:", fourth_node.data)
structure.print_structure()

print("\nElemento eliminado:", structure.pop())

print("Estructura después de pop:")
structure.print_structure()
