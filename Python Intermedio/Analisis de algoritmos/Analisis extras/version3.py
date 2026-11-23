# Complejidad temporal:
# Mejor caso: O(1), si encuentra el elemento en la primera posición.
# Caso promedio: O(n), porque puede recorrer una parte considerable
# de la lista antes de encontrar el elemento.
# Peor caso: O(n), si el elemento está al final o no existe.

# Complejidad espacial: O(1)
# Utiliza una variable para recorrer la lista y no crea estructuras
# adicionales que dependan del tamaño de la entrada.

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

list_to_search = [1, 2, 3, 4, 5, 6]
target_value = 4
if linear_search(list_to_search, target_value):
    print(f"El valor {target_value} se encuentra en la lista.")
else:
    print(f"El valor {target_value} no se encuentra en la lista.")