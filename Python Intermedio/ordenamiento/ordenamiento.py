def bubble_sort(list_to_sort):
        
    for outer_index in range(0, len(list_to_sort) - 1):
        
        swapped = False
        
        #Recorremos la lista de derecha a izquierda, comenzando desde 
        # #el último índice hasta el índice 1, reduciendo el índice 
        # en cada iteración.
        for index in range(len(list_to_sort) - 1, outer_index, -1):

            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]

            print(
                f"-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {previous_element}"
            )

            # Si el actual es menor  al siguiente, intercambiamos sus posiciones
            if current_element < previous_element:

                print(
                    "El elemento actual es menor al siguiente. Moviemndo elmento a la izquierda"
                )
                
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = current_element
                
                swapped = True
        # Si no hubo intercambio, la lista ya esat ordenada.
        if not swapped:
            print("No hubo intercambios. La lista ya está ordenada.")
            break

# Caso 1: Lista en orden inverso
my_numbers_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(my_numbers_list)
print("\nLista invertida:", my_numbers_list)

# Caso 2: Lista ya ordenada
my_numbers_list = [1, 2, 3, 4, 5]
bubble_sort(my_numbers_list)
print("\nLista ordenada:", my_numbers_list)

# Caso 3: Lista con números repetidos
my_numbers_list = [4, 2, 4, 1, 2]
bubble_sort(my_numbers_list)
print("\nLista con repetidos:", my_numbers_list)

# Caso 4: Lista con un solo elemento
my_numbers_list = [7]
bubble_sort(my_numbers_list)
print("\nLista con un elemento:", my_numbers_list)
