print("-----Buscar números repetidos-----")
my_list = [4, 2, 7, 2, 8, 2, 1]


target_number = int(input(f"Ingrese el número que desea buscar: "))

count = 0     

for number in my_list:
        if number == target_number:
            count+=1
        
print()
        
if count > 0:
    print(f"EL número {target_number} aparece {count} veces.")
else:
    print(f"El número {target_number} no se encuentra en la lista")