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

    def append(self, data):
        node = Node(data)

        if self.head is None:
            # Con lista vacia tail head apuntan el primer nodo
            self.head = node
            self.tail = node

        else:
            # Conecta al ultimo nodo con el nuevo nodo.
            self.tail.next = node
            # Conecta al nuevo nodo con el anterior.
            node.prev = self.tail
            # apuntamos tail hacia el nuevo nodo
            self.tail = node


dll = Double_list()

dll.append("A")
dll.append("B")
dll.append("C")
