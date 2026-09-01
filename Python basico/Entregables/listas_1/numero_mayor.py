print("Ingrese 10 números para determinar cuál es el mayor.")
print()
major = 1
count = 1
numbers_list = []
for i in range(1,11):
    num= int(input(f"Ingrese el número {count}: "))
    numbers_list.append(num)
    count += 1
    
    if num > major:
        major = num
print()
print(f"La lista es: {numbers_list}")
print(f"El número mayor es: {major}")
