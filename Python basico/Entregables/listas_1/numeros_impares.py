import random
print("-----Removiendo números impares de una lista-----")
my_list = [random.randint(1,100) for i in range(10)]
print(f"Acabo de generar una lista de 10 números aleatorios: {my_list}")
print("Removiendo los números impares de la lista...")
print()
new_list = []
for number in my_list:
    if number % 2 == 0:
        new_list.append(number)
print(f"Removi los números impares de la lista: {new_list}")