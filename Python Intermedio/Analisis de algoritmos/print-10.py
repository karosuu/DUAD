# Complejidad temporal: O(1)
# El ciclo realiza como máximo 5 iteraciones, independientemente
# del tamaño de la lista. La función len() y min() son operaciones
# constantes.
#
# Complejidad espacial: O(1)
# No crea estructuras adicionales que dependan del tamaño de la lista.

def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 5)):
        print(list_to_print[index])


list_to_print = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print_10_or_less_elements(list_to_print)
