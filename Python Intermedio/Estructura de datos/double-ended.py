class Node:
    data: str
    next: "Node | None"
    prev: "Node | None"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    # head y tail pueden referenciar  Node o None
    head: Node | None
    tail: Node | None

    def __init__(self):
        # inicializamos head y tail como None
        self.head = None
        self.tail = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, node):

        if self.head is None:
            # La deque está vacía.
            # El nuevo nodo será el primero y el último.
            self.head = node
            self.tail = node

        else:
            # Conectamos el nuevo nodo con el primer nodo actual.
            # node.next apunta al nodo que anteriormente era head.
            node.next = self.head

            # Establecemos la conexión inversa.
            self.head.prev = node
            # Actualizamos head para que apunte al nuevo nodo.
            self.head = node

    def push_right(self, node):

        if self.tail is None:

            self.head = node
            self.tail = node

        else:
            # Conecatmos el antiguo nodo con el nuevo.
            self.tail.next = node

            # Establecemos la conexion inversa.
            node.prev = self.tail
            # Actualizamos tail para que apunte al nuevo último nodo.
            self.tail = node

    def pop_left(self):
        # Comprobamos si la deque está vacía.
        if self.head is None:
            return
        # Movemos head al siguiente nodo.
        self.head = self.head.next
        # Comprobamos si la deque quedó vacía.
        if self.head is None:
            self.tail = None

        else:
            # El nuevo primer nodo no debe tener un nodo anterior.
            self.head.prev = None

    def pop_right(self):
        # Comprobamos si la deque está vacía.
        # Si tail es None, no hay ningú
        if self.tail is None:
            return
        # Movemos tail al nodo anterior al último.
        # De esta manera, el penúltimo nodo pasa a ser el último.
        self.tail = self.tail.prev

        # Comprobamos si tail quedó en None.
        # Esto significa que acabamos de eliminar el único nodo
        # que había en la deque, por lo que head también debe ser None.
        if self.tail is None:
            self.head = None

        else:
            # Si todavía quedan nodos, eliminamos la conexión
            # hacia el nodo que acabamos de quitar.
            # El nuevo último nodo ya no debe apuntar a ningún nodo siguiente.
            self.tail.next = None


print("\n========== PRUEBA 1: PUSH LEFT ==========")

deque_left = Deque()

deque_left.push_left(Node("B"))
deque_left.push_left(Node("A"))
deque_left.push_left(Node("Inicio"))


print("Resultado obtenido:")
deque_left.print_structure()


print("\n========== PRUEBA 2: PUSH RIGHT ==========")

deque_right = Deque()

deque_right.push_right(Node("A"))
deque_right.push_right(Node("B"))
deque_right.push_right(Node("Final"))


print("Resultado obtenido:")
deque_right.print_structure()

print("\n========== PRUEBA 3: POP LEFT ==========")

deque = Deque()

# Caso 1: deque vacía
print("\nCaso 1: Deque vacía")
deque.pop_left()
deque.print_structure()
print("Prueba completada sin errores.")


# Caso 2: deque con un solo nodo
print("\nCaso 2: Un solo nodo")
deque.push_right(Node("A"))
deque.print_structure()

deque.pop_left()

print("Después de eliminar el único nodo:")
deque.print_structure()
print("Head:", deque.head)
print("Tail:", deque.tail)


# Caso 3: deque con varios nodos
print("\nCaso 3: Varios nodos")

deque.push_right(Node("A"))
deque.push_right(Node("B"))
deque.push_right(Node("C"))

print("Antes de eliminar:")
deque.print_structure()

deque.pop_left()

print("Después de eliminar el primer nodo:")
deque.print_structure()
