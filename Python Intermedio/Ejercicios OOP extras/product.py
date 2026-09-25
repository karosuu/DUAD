class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    # Agrega los productos a la lista
    def add_products(self, product):
        self.products.append(product)

    def show_all_products(self):
        for product in self.products:
            print(
                "\nNombre:",
                product.name,
                "\nPrecio:",
                product.price,
                "\nCantidad:",
                product.quantity,
            )

    def calculate_total_value(self):
        total = 0

        for product in self.products:
            total = total + product.price * product.quantity

        return total


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

# Crea el inventario
inventory = Inventory()
inventory.add_products(product1)
inventory.add_products(product2)
inventory.show_all_products()
print(f"\nEl valor total del inventario es: {inventory.calculate_total_value()}" )
