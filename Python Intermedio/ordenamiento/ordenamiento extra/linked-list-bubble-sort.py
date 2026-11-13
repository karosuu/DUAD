class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head = Node | None

    def __init__(self, head=None):
        self.head = head

    def insert_front(self, data):
        # Crea el nuevo nodo y lo asigna al head.
        node = Node(data)
        # El nuevo nodo apunta al inicio de la cola.
        node.next = self.head
        # El nuevo nodo se convierte en el primero de la lista.
        self.head = node
    
    def insert_back(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node

    def bubble_sort(self):
        swapped = True

        while swapped:
            swapped = False
            current_node = self.head

            while current_node is not None and current_node.next is not None:

                print(
                    f"Actual: {current_node.data}, Siguiente: {current_node.next.data}"
                )

                if current_node.data > current_node.next.data:
                    temp = current_node.data
                    current_node.data = current_node.next.data
                    current_node.next.data = temp

                    swapped = True

                current_node = current_node.next
    def delete(self, data):
        if self.head is None:
            return

        # Compara el valor del nodo almacenado con el que quiero eliminar.
        if self.head.data == data:
            # Actualiza self.head al siguiente nodo
            self.head = self.head.next
            return

        # Si el valor no esta en la lista iniciamos
        # el recorrido desde self.head
        current_node = self.head

        # Recorre la lista mientras el siguiente nodo exista
        # y su valor sea diferente al que queremos eliminar.
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next

        # Si el siguiente nodo existe, lo elimina enlazando el nodo actual
        # directamente con el nodo que viene después del que queremos eliminar.
        if current_node.next is not None:
            current_node.next = current_node.next.next            

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()


ll = LinkedList()

ll.insert_back(5)
ll.insert_back(2)
ll.insert_back(8)
ll.insert_back(1)

print("Metodo insert_back")
ll.print_all()

ll = LinkedList()

ll.insert_front(5)
ll.insert_front(2)
ll.insert_front(8)
ll.insert_front(1)

print("\nMetodo insert_front")
ll.print_all()


print("\nMetodo bubble_sort")
ll.bubble_sort()
ll.print_all()

ll = LinkedList()

ll.insert_back(5)
ll.insert_back(2)
ll.insert_back(8)

ll.delete(5)
print("\n borra el primer elemento")
ll.print_all()

# Expected: 2 -> 8