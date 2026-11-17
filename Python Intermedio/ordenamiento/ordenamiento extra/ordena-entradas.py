
def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort) - 1):
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            if list_to_sort[index] < list_to_sort[index - 1]:
                list_to_sort[index], list_to_sort[index - 1] = list_to_sort[index - 1], list_to_sort[index]

    return list_to_sort


def validated_bubble_sort(list_to_sort):

    if len(list_to_sort) == 0:
        raise ValueError("Error: La lista está vacía")

    for element in list_to_sort:
        if isinstance(element, bool) or not isinstance(element, (int, float)):
            raise ValueError("Error: La lista contiene elementos no numéricos")

    return bubble_sort(list_to_sort)


# Prueba
try:
    print(validated_bubble_sort([5, 3, 8, "hola", 2, 7, 9]))
except ValueError as error:
    print(error)
 