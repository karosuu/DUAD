class Node:
    data: str
    next: "Node | None"
    prev: "Node | None"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Double_list:
    head: Node | None
    tail: Node | None

    def __init__(self):
        self.head = None
        self.tail = None

    # Agrega elementos al final de la lista.
    def append(self, data):
        node = Node(data)

        if self.head is None:
            # Con lista vacía tail head apuntan el primer nodo
            self.head = node
            self.tail = node

        else:
            # Conecta al ultimo nodo con el nuevo nodo.
            self.tail.next = node
            # Conecta al nuevo nodo con el anterior.
            node.prev = self.tail
            # apuntamos tail hacia el nuevo nodo
            self.tail = node

    # Agrega elementos al inicio de la lista.
    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            # Conectamos el nuevo nodo con el primer nodo actual.
            # El siguiente nodo del nuevo nodo será el antiguo head.
            node.next = self.head

            # Conectamos el antiguo primer nodo con el nuevo nodo.
            # Su referencia prev apuntará al nuevo nodo.
            self.head.prev = node

            self.head = node

    def print_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()

    def print_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.prev is not None:
                print(" -> ", end="")

            current_node = current_node.prev

        print()

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            # Actualiza self.head al siguiente nodo
            self.head = self.head.next

            if self.head is None:
                # La lista quedo vacía.
                self.tail = None

            else:
                # El nuevo primer nodo no debe apuntar al nodo anterior.
                self.head.prev = None
            return

        # Si el valor no esta en la lista iniciamos
        # el recorrido desde self.head
        current_node = self.head

        # Recorre la lista mientras el siguiente nodo exista
        # y su valor sea diferente al que queremos eliminar.
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next

        # Comprueba si encontramos el valor.
        if current_node.next is None:
            return
        
        # Comprueba si el nodo que queremos eliminar es el último.
        if current_node.next.next is None:
            
            # Actualiza tail al nuevo último nodo.
            self.tail = current_node
            
            # Desconecta el ultimo nodo
            current_node.next = None
        
        else:
            # Conecta el nodo actual con el siguiente al que queremos eliminar.         
            current_node.next = current_node.next.next
            
            # Actualiza la referencia prev del nodo siguiente.
            current_node.next.prev = current_node


# ==========================================
# PRUEBA 1: Insertar elementos
# ==========================================

dll = Double_list()

dll.append("A")
dll.append("B")
dll.append("C")

print("Prueba 1 - Recorrido hacia adelante:")
dll.print_forward()  

print("Prueba 2 - Recorrido hacia atrás:")
dll.print_backward()  


# ==========================================
# PRUEBA 3: Eliminar un nodo intermedio
# ==========================================

print("\nPrueba 3 - Eliminar B:")
dll.delete("B")

dll.print_forward()  
dll.print_backward()  


# ==========================================
# PRUEBA 4: Eliminar el último nodo
# ==========================================

print("\nPrueba 4 - Eliminar C:")
dll.delete("C")

dll.print_forward()  
dll.print_backward()  

print("Head:", dll.head.data)  
print("Tail:", dll.tail.data)  


# ==========================================
# PRUEBA 5: Eliminar el único nodo
# ==========================================

print("\nPrueba 5 - Eliminar A:")
dll.delete("A")

dll.print_forward()   
dll.print_backward()  

print("Head:", dll.head)  
print("Tail:", dll.tail)  


# ==========================================
# PRUEBA 6: Eliminar un valor inexistente
# ==========================================

print("\nPrueba 6 - Eliminar un valor inexistente:")

dll.append("X")
dll.append("Y")

dll.delete("Z")

dll.print_forward()  
dll.print_backward()  


# ==========================================
# PRUEBA 7: Eliminar el primer nodo
# ==========================================

print("\nPrueba 7 - Eliminar el primer nodo:")

dll.delete("X")

dll.print_forward()   
dll.print_backward()  

print("Head:", dll.head.data)  
print("Tail:", dll.tail.data)  


# ==========================================
# PRUEBA 8: Eliminar el último nodo
# ==========================================

print("\nPrueba 8 - Eliminar el último nodo:")

dll.append("Z")
dll.delete("Z")

dll.print_forward()   
dll.print_backward()  

print("Head:", dll.head.data)  
print("Tail:", dll.tail.data)  