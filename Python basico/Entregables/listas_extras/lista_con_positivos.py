print('-----Lista verifica si hay al menos un numero negativo-----')
my_list = []

for i in range (5):
    number = int(input(f"Ingrese el número {i + 1}: "))
    my_list.append(number)


negative_number = False
for x in my_list:
    if x < 0:
        negative_number = True
        break

if negative_number:
    print("Hay al menos un número negativo en la lista.")
else:
    print("No hay números negativos en la lista.")
