import random

print('-----Calcular el promedio y encontrar números mayor promedio-----')
print()
random_numbers = [random.randint(1, 50) for _ in range(8)]

print(f"Números generados: {random_numbers}")
print()

average = sum(random_numbers) / len(random_numbers)
highest_numbers = [num for num in random_numbers if num > average]
print(f"Promedio de los números generados: {average}")
print(f"Números mayores al promedio: {highest_numbers}")