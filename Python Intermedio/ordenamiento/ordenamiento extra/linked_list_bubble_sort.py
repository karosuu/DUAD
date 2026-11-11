def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        # Recorremos la lista de derecha a izquierda, comenzando desde
        # #el último índice hasta el índice 1, reduciendo el índice
        # en cada iteración.
        for index in range(len(list_to_sort) - 1, outer_index, -1):

            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]

            print(
                f"-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {previous_element}"
            )

            # Si el actual es mayor al siguiente, intercambiamos sus posiciones
            if current_element < previous_element:

                print(
                    "El elemento actual es menor al siguiente. Moviemndo elmento a la izquierda"
                )
                temp = current_element
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = temp

    return list_to_sort

linked_list = [5, 2, 8, 1]


print(bubble_sort(linked_list))
