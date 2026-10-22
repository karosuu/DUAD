class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head = Node | None

    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self, data):
        node = Node(data)
        
        # Caso 1: la cola está vacía
        # Si la cola tiene A return evita que siga recorriendo
        if self.head is None:
            self.head = node
            return

        # Caso 2: la cola ya tiene elementos
        current_node = self.head

        # Recorrer hasta encontrar el último nodo
        while current_node.next is not None:
            current_node = current_node.next

        # Enlazar el último nodo con el nuevo
        current_node.next = node

    def dequeue(self):
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        return data

    def print_all(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data, end="")
            
            if current_node.next is not  None:
                print(" -> ", end="")
                
            current_node = current_node.next
            
        print()
    
# Crear una cola vacía
q = Queue()

print("1. Cola vacía:")
q.print_all()

# Agregar elementos
print("\n2. Agregando A, B y C:")
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()

# Eliminar el primer elemento
print("\n3. Eliminar el primer elemento:")
removed = q.dequeue()
print("Elemento eliminado:", removed)

print("Cola restante:")
q.print_all()

# Agregar otro elemento
print("\n4. Agregar D:")
q.enqueue("D")
q.print_all()
