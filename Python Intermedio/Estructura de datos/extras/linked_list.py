class Node:
    data: str
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
        # El nuevo nodo apunta al incio de la cola.
        node.next = self.head
        # El nuevo nodo se convierte en el primero de la lista.
        self.head = node

    def insert_back(self, data):
        node = Node(data)

        # Comprueba que la lista esta vacia.
        # Si esta vacia asigna self.head al nuevo nodo.
        if self.head is None:
            self.head = node
            return

        current_node = self.head

        # Recorre la lista utilizando current_node
        # hasta encontrar el último nodo.
        while current_node.next is not None:
            current_node = current_node.next

        # Enloaza el ultimo nodo con el nuevo nodo
        current_node.next = node

    def delete(self, data):
        if self.head is None:
            return

        # Compara el valor del nodo almacenado con el que quiero eliminar.
        if self.head.data == data:
            # Actualiz self.head al siguiente nodp
            self.head = self.head.next
            return

        # Si el valor no esta en la lista iniciamos
        # el rwecorrido desde self.head
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
        pass


ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)
ll.print_all()
