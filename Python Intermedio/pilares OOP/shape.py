from abc import ABC, abstractmethod
import math


# Se agrega ABC a la clase para establecer relacion con el metodo abstrato
class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius

        return perimeter

    def calculate_area(self):
        area = math.pi * (self.radius**2)

        return area


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4 * self.side

        return perimeter

    def calculate_area(self):
        area = self.side * self.side

        return area


class Rectangle(Shape):
    def __init__(self, height, width):
        if width < 0 or height < 0:
            raise ValueError("El valor no puede ser negativo")
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)

        return perimeter

    def calculate_area(self):
        area = self.width * self.height

        return area


def show_menu():
    print("\n1. Selecciona circulo")
    print("2. Selecciona cuadrado")
    print("3. Selecciona rectangulo")
    print("4. Salir")

    while True:
        try:
            option = int(input("\nSeleccione una opcion: "))
        except ValueError as error:
            print(f"Opcion no valida {error}")
            continue

        if 1 <= option <= 4:
            return option
        else:
            print("Opcion nmo valida")


def main():
    option = 0
    while option != 4:
        option = show_menu()

        if option == 1:
            radius = float(input("Ingrese el radio del círculo: "))

            circle = Circle(radius)

            area = circle.calculate_area()
            perimeter = circle.calculate_perimeter()

            print(f"Área: {area}")
            print(f"Perímetro: {perimeter}")

        elif option == 2:
            side = float(input("Ingrese el lado del cuadrado: "))

            square = Square(side)

            area = square.calculate_area()
            perimeter = square.calculate_perimeter()

            print(f"Área: {area}")
            print(f"Perímetro: {perimeter}")

        elif option == 3:
            height = float(input("Ingrese la altura: "))
            width = float(input("Ingrese el ancho: "))

            rectangle = Rectangle(height, width)

            area = rectangle.calculate_area()
            perimeter = rectangle.calculate_perimeter()

            print(f"Área: {area}")
            print(f"Perímetro: {perimeter}")

        elif option == 4:
            break


if __name__ == "__main__":
    main()
