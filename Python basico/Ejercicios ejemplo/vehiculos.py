vehicle_quantity = int(input("How many vehicles do you want to enter?: "))

print()
details = []

for i in range(vehicle_quantity):
    print(f"Vehicle number {i + 1}")
    brand = input("Enter the vehicle brand: ")
    model = input("Enter the vehicle model: ")
    year = int(input("Enter the vehicle year: "))
    color = input("Enter the vehicle color: ")
    price = int(input("Enter the vehicle price: "))
    transmission = input("Enter the vehicle transmission type (manual/automatic): ")
    print()

    detail = {
        "brand": brand,
        "model": model,
        "year": year,
        "color": color,
        "price": price,
        "transmission": transmission
    }

    details.append(detail)

vehicle = {
    "quantity": vehicle_quantity,
    "details": details
}

edit = input("Do you want to edit a vehicle? (yes/no): ").lower()

if edit == "yes":
    vehicle_number = int(input("Enter the vehicle number you want to edit: ")) - 1
    field = input("Enter the field you want to edit (brand, model, year, color, price, transmission): ").lower()
    new_value = input("Enter the new value: ")

    if field == "brand":
        new_value = new_value.lower()
    elif field == "model":
        new_value = new_value.lower()
    elif field == "year":
        new_value = int(new_value)
    elif field == "color":
        new_value = new_value.lower()
    elif field == "price":
        new_value = int(new_value)
    elif field == "transmission":
        new_value = new_value.lower()

    vehicle["details"][vehicle_number][field] = new_value

print()
print("-----Vehicle Information-----")

for i, detail in enumerate(vehicle["details"], start=1):
    print(f"Vehicle {i}:")
    print(f"Brand: {detail['brand']}")
    print(f"Model: {detail['model']}")
    print(f"Year: {detail['year']}")
    print(f"Color: {detail['color']}")
    print(f"Price: {detail['price']}")
    print(f"Transmission: {detail['transmission']}")
    print("-------------------------------")