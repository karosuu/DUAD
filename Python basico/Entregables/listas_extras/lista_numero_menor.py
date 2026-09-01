print("----Busca el numero mas pequeño de la lista----")
my_list = []

for i in range(5):
    number = int(input(f"Ingrese el número {i + 1}: "))
    my_list.append(number)
    
smallest_number = my_list[0]
for x in my_list:
    if x < smallest_number:
        smallest_number = x
        
print(f"El número más pequeño de la lista es: {smallest_number}")