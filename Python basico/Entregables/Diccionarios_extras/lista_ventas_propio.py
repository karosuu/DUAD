sales =  []

num_sales = int(input("Cuantas ventas desea ingresar: "))

print()

for i in range (num_sales):
    print(f" -- Venta #{i + 1} --")
    
    sale = {}
    
    sale["date"] =  input("Ingrese la fecha (dd/mm/aa): ")
    sale["customer_email"] = input('Ingrese el correo del cliente: ')  
    
    sale["items"] = []
    
    num_items = int(input("Cuantos productos tiene esta venta?:" ))
    
    
    for j in range (num_items):
        print(f"Producto #{j + 1}")
        
        item= {}
    
        item["name"] = input("Nombre del producto: ")
        item["upc"] = input("UPC del producto: ")
        item["unit_price"] =  float(input("Precio unitario: "))
        
        sale["items"].append(item)
        
    sales.append(sale)
print()  
print("==== Ventas Registradas ====")

for sale in sales:

    print(f"\nFecha: {sale['date']}")
    print(f"Cliente: {sale['customer_email']}")

    for item in sale["items"]:
        print(f"Producto: {item['name']}")
        print(f"UPC: {item['upc']}")
        print(f"Precio: ${item['unit_price']}")