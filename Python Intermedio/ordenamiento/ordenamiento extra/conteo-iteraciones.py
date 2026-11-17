class Node:
    data: str
    next: "Node | None"
    prev: "Node | None"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:

    head: Node | None
    tail: Node | None

    def __init__(self):
        self.head = None
        self.tail = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def bubble_sort(self):

        # Si la Deque está vacía, no hay elementos que ordenar.
        if self.head is None:
            return 0, 0

        # Límite de la parte que ya está ordenada.
        end_node = None

        # Contadores de iteraciones e intercambios.
        iterations = 0
        swaps = 0

        # Repetimos las pasadas hasta ordenar la Deque.
        while end_node != self.head:

            # Indicamos si hubo intercambios.
            swapped = False

            # Comenzamos desde el primer nodo.
            current_node = self.head

            # Recorremos los nodos hasta el límite.
            while current_node.next != end_node:

                next_node = current_node.next

                # Comparamos los valores de los nodos.
                if current_node.data > next_node.data:

                    # Intercambiamos los valores.
                    current_node.data, next_node.data = (
                        next_node.data,
                        current_node.data
                    )

                    # Contamos el intercambio.
                    swaps += 1
                    swapped = True

                # Avanzamos al siguiente nodo.
                current_node = current_node.next

            # Contamos la pasada realizada.
            iterations += 1

            # Actualizamos el límite de la parte ordenada.
            end_node = current_node

            # Si no hubo intercambios, ya está ordenada.
            if not swapped:
                break

        # Retornamos los contadores.
        return iterations, swaps

    def push_left(self, node):

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def push_right(self, node):

        if self.tail is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node



# CASO 1: DEQUE EN ORDEN INVERSO
deque_reverse = Deque()

deque_reverse.push_right(Node("5"))
deque_reverse.push_right(Node("4"))
deque_reverse.push_right(Node("3"))
deque_reverse.push_right(Node("2"))
deque_reverse.push_right(Node("1"))

print("\nCaso 1: Orden inverso")

iterations, swaps = deque_reverse.bubble_sort()

print("Lista ordenada:")
deque_reverse.print_structure()

print("Iteraciones:", iterations)
print("Intercambios:", swaps)



# CASO 2: DEQUE YA ORDENADA
deque_sorted = Deque()

deque_sorted.push_right(Node("1"))
deque_sorted.push_right(Node("2"))
deque_sorted.push_right(Node("3"))
deque_sorted.push_right(Node("4"))
deque_sorted.push_right(Node("5"))

print("\nCaso 2: Lista ya ordenada")

iterations, swaps = deque_sorted.bubble_sort()

print("Lista ordenada:")
deque_sorted.print_structure()

print("Iteraciones:", iterations)
print("Intercambios:", swaps)


# CASO 3: DEQUE CON ELEMENTOS REPETIDOS
deque_duplicates = Deque()

deque_duplicates.push_right(Node("4"))
deque_duplicates.push_right(Node("2"))
deque_duplicates.push_right(Node("4"))
deque_duplicates.push_right(Node("1"))
deque_duplicates.push_right(Node("2"))

print("\nCaso 3: Elementos repetidos")

iterations, swaps = deque_duplicates.bubble_sort()

print("Lista ordenada:")
deque_duplicates.print_structure()

print("Iteraciones:", iterations)
print("Intercambios:", swaps)



# CASO 4: DEQUE CON UN SOLO ELEMENTO
deque_single = Deque()

deque_single.push_right(Node("7"))

print("\nCaso 4: Un elemento")

iterations, swaps = deque_single.bubble_sort()

print("Lista ordenada:")
deque_single.print_structure()

print("Iteraciones:", iterations)
print("Intercambios:", swaps)



# CASO 5: DEQUE VACÍA
deque_empty = Deque()

print("\nCaso 5: Deque vacía")

iterations, swaps = deque_empty.bubble_sort()

print("Lista ordenada:")
deque_empty.print_structure()

print("Iteraciones:", iterations)
print("Intercambios:", swaps)



# CASO 6: EJEMPLO DEL EJERCICIO
deque_example = Deque()

deque_example.push_right(Node("5"))
deque_example.push_right(Node("1"))
deque_example.push_right(Node("4"))
deque_example.push_right(Node("2"))
deque_example.push_right(Node("3"))

print("\nCaso 6: Ejemplo del ejercicio")

iterations, swaps = deque_example.bubble_sort()

print("Lista ordenada:")
deque_example.print_structure()

print("Iteraciones:", iterations)
print("Intercambios:", swaps)