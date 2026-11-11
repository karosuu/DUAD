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

print("Metodo insert back")
ll.print_all()

print("\nMetodo bubble_sort")
ll.bubble_sort()
ll.print_all()
