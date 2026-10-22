class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Vehiculo: {self._brand}, año: {self._year}"


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        self.doors = doors

        super().__init__(brand, year)

    def get_info(self):
        return f"Vehiculo: {self._brand}, Año: {self._year}, Puertas: {self.doors} "


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        self.type = type

        super().__init__(brand, year)

    def get_info(self):
        return f"Vehiculo: {self._brand}, Año: {self._year}, Tipo: {self.type} "


vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print (vehicle1.get_info())
print(vehicle2.get_info())