#En este ejercicio no se ejecuta la opcion de bajar. 

#class Person:
def __init__(self, passenger_name):
        self.passenger_name = passenger_name


class Bus:
    def __init__(self, max_passangers):
        # Valida la cantidad de N de pasajeros que determina el usuario
        self.max_passangers = max_passangers
        self.passenger = []

    # Agrega pasajeros
    def add_passenger(self, person):
        if len(self.passenger) < self.max_passangers:
            self.passenger.append(person)
        else:
            print("El bus esta lleno")

    # Remueve pasajeros
    def remove_passenger(self, person):
        if person in self.passenger:
            self.passenger.remove(person)
        else:
            print("El pasajero no esta en la lista")


# Cantidad máxima de pasajeros
max_passangers = input("Cuantos pasajero quiere agregar: ")
max_passangers = int(max_passangers)
bus = Bus(max_passangers)


# Agregar pasajeros
def get_names(bus):
    count = 1
    # Para probar el else solo agregar + 1 en el while luego de max_passengers
    while count <= max_passangers:
        passenger_name = input(f"Ingrese el nombre del pasajero {count}: ")
        person = Person(passenger_name)
        bus.add_passenger(person)
        count += 1

get_names(bus)