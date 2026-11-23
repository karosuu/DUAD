# Complejidad temporal:
# Mejor caso: O(1), si encuentra el elemento en la primera iteración.
# Caso promedio: O(log n), porque reduce el espacio de búsqueda
# a la mitad en cada iteración.


# Complejidad espacial: O(1)
# Utiliza únicamente variables auxiliares y no crea estructuras
# adicionales que dependan del tamaño de la entrada.

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

list_to_search = [1, 2, 3, 4, 5, 6]
target_value = 4
if binary_search(list_to_search, target_value):
    print(f"El valor {target_value} se encuentra en la lista.")
else:
    print(f"El valor {target_value} no se encuentra en la lista.")