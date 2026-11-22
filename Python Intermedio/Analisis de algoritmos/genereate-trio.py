# Complejidad temporal: O(a * b * c)
# Utiliza tres ciclos anidados que recorren las listas list_a, list_b
# y list_c. Por cada elemento de list_a, recorre todos los elementos
# de list_b y list_c, generando a * b * c combinaciones.
#
# Complejidad espacial: O(a * b * c)
# Almacena todas las combinaciones generadas en result_list.


def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f"{element_a} {element_b} {element_c}")

    return result_list


list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
list_c = ["x", "y", "z"]

print(generate_list_trios(list_a, list_b, list_c))
