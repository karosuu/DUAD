addition = 0
count = 1
num=int(input("Ingrese un número: "))
while count <= num:
    addition = addition + count
    count += 1
print(f"La suma de los números del 1 al {num} es: {addition}")
