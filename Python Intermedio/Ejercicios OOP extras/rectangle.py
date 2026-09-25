class Rectangle:
    def __init__(self, height, width):
        # Valida que los valores no sera negativos
        if width < 0 or height < 0:
            raise ValueError("El valor no puede ser negativo")
        self.width = width
        self.height = height

    # Calcula el Area
    def get_area(self):
        area = self.width * self.height
        return area

    # Calcula de perimetro
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter


def data_input():
    print("----Calcula el area y perimetro de un rectangulo----")
    
    # Solicita valores al usaurio
    width = float(input("Ingrese el ancho: "))
    height = float(input("Ingrese la altura: "))
    
    return height, width

#obtiene los valores ingresados
height, width= data_input()

try:
    # crea el objeto
    rectangle_measurements = Rectangle(height, width)

    print(f"\nEl area del rectangulo es {rectangle_measurements.get_area()}")
    print(f"El perimetro del rectangulo es {rectangle_measurements.get_perimeter()}")

except ValueError:
    print("El valor no puede ser negativo")