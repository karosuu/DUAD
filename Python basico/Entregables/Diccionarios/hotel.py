print("-----Este programa permite crear un diccionario de hoteles-----")

print()
name = input("Ingrese el nombre del hotel: ")
stars_rate = int(input("Ingrese la calificación del hotel (1-5): "))   
print()
rooms = []

room_quantity = int(input("Cuantas habitaciones tiene el hotel?: "))

for i in range (room_quantity):
    print(f"-----Habitación {i + 1}-----")

    number = int(input("Ingrese el número de la habitación: "))
    floor = int(input("Ingrese el piso de la habitación: "))
    price_per_night = float(input("Ingrese el precio por noche de la habitación: "))

    room = {
    "number": number,
    "floor": floor,
    "price_per_night": price_per_night
    }

    rooms.append(room)

hotel = {
    "name": name,
    "stars_rate": stars_rate,
    "rooms": rooms
}

print()
print("-----Información del hotel-----")
print(f"Nombre del hotel: {hotel['name']}")
print(f"Calificación del hotel: {hotel['stars_rate']} estrellas")
print()

print(f"Habitaciones del hotel: {len(hotel['rooms'])}")
for room in hotel['rooms']:
    print(f"Numero: {room['number']}")
    print(f"Piso: {room['floor']}")
    print(f"Precio por noche: {room['price_per_night']}")
    print("---------------------------")
    