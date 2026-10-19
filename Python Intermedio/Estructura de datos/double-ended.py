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

print("Prueba de push left: ")
deque_left = Deque()

third_node = Node("Tercer nodo C")
deque_left.push_left(third_node)

second_node = Node("Segundo nodo B")
deque_left.push_left(second_node)

first_node = Node("Primer nodo A")
deque_left.push_left(first_node)
deque_left.print_structure()



print("\nPrueba de push right: ")
deque_right = Deque()

third_node = Node("Tercer nodo C")
deque_right.push_right(third_node)

second_node = Node("Segundo nodo B")
deque_right.push_right(second_node)

first_node = Node("Primer nodo A")
deque_right.push_right(first_node)
deque_right.print_structure()