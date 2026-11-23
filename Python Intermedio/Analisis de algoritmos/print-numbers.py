# Complejidad temporal: O(n)
# Recorre la lista una sola vez y realiza una operación constante
# (multiplicar por 2 e imprimir) por cada elemento.
#
# Complejidad espacial: O(1)
# No crea estructuras adicionales que dependan del tamaño de la lista.


def print_numbers_times_2(numbers_list):
    for number in range(len(numbers_list)):

        print(numbers_list[number] * 2)

    return numbers_list

numbers = [1, 2, 3, 4, 5]
print_numbers_times_2(numbers)