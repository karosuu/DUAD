class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, node):
        # Conecta el nuevo nodo con la cima actual. 
        #  Si la pila está vacía, node.next será None.
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            # Guarda el valor del nodo que se va a eliminar.
            previous_head = self.head.data
            # Actualiza la cima para que apunte al siguiente nodo.
            # De esta manera, el nodo anterior deja de pertenecer a la pila.
            self.head = self.head.next

            return previous_head

        else:
            raise ValueError("No se puede eliminar un elemento de una pila vacía.")


# first_node = Node("Hola")
# second_node = Node("Mundo")
# first_node.next = second_node
# third_node = Node("Python")
# second_node.next = third_node
# fourth_node = Node("New")

# structure = Stack(first_node)
# structure.push(fourth_node)

# print("\nElemento agregado:", fourth_node.data)
# structure.print_structure()

# print("\nElemento eliminado:", structure.pop())
# print("Estructura después de pop:")
# structure.print_structure()

# Crear una pila vacía
structure = Stack()

try:
    # Intentar eliminar un elemento de la pila vacía
    structure.pop()

except ValueError as error:
    print("Error:", error)

# Continuar ejecutando el programa
print("\nPrueba finalizada.")


# Imprimir la pila vacía
print("Pila vacía:")
structure.print_structure()

# Crear un nodo y agregarlo
first_node = Node("Hola")
structure.push(first_node)

print("\nDespués de agregar Hola:")
structure.print_structure()

# Agregar dos nodos más
second_node = Node("Mundo")
structure.push(second_node)

third_node = Node("Python")
structure.push(third_node)

print("\nDespués de agregar Mundo y Python:")
structure.print_structure()

# Eliminar un elemento
removed_element = structure.pop()
print("\nElemento eliminado:", removed_element)

# Mostrar la pila después de eliminar
print("\nPila después de pop:")
structure.print_structure()
