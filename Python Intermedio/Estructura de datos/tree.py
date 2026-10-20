class Node:
    data: int
    left: "Node | None"
    right: "Node | None"

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    root: Node | None

    def __init__(self):
        self.root = None

    def print_structure(self):
        self._print_node(self.root)

    def _print_node(self, node):
        if node is None:
            return

        print(node.data)
        self._print_node(node.left)
        self._print_node(node.right)

    def binary_left(self, node):
        self.root.left = node

    def binary_right(self, node):
        self.root.right = node


binarytree = BinaryTree()

first_node = Node(10)

second_node = Node(5)

third_node = Node(15)

fourth_node = Node(20)

fifth_node = Node(25)

sixth_node = Node(30)


binarytree.root = first_node

binarytree.binary_left(second_node)

second_node.left = fourth_node
second_node.right = fifth_node

binarytree.binary_right(third_node)

third_node.right = sixth_node

binarytree.print_structure()
