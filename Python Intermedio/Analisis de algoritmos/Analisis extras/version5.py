# Complejidad temporal: O(n²)
# Utiliza dos ciclos anidados que recorren todas las claves del
# diccionario. Por cada clave del primer ciclo, recorre nuevamente
# todas las claves, generando n * n combinaciones.
#
# Complejidad espacial: O(1)
# No crea estructuras adicionales que dependan del tamaño
# del diccionario.


def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

my_dict = {'a': 1, 'b': 2, 'c': 3}
print_all_pairs(my_dict)
