class Person():
    def __init__(self, passenger_name):
        self.passenger_name = passenger_name


class Bus:
    def __init__(self, max_passangers):
        
        self.max_passangers = max_passangers
        self.passenger = []
        

    def add_passenger(self, person ):
        if len(self.passenger) < self.max_passangers:
            self.passenger.append(person)
        else:
            print("El bus esta lleno")

max_passangers = input("Cuantos pasajero quiere agregar: ")
max_passangers = int(max_passangers)
bus = Bus(max_passangers)

def get_names(bus):
    count = 1
        #El mas para probar el else solo agregar + 1 en el while luego de max_passengers
    while count <= max_passangers:
        passenger_name = input(f"Ingrese el nombre del pasajero {count}: ")
        person = Person(passenger_name)
        bus.add_passenger(person)
        count +=1 
        
get_names(bus)