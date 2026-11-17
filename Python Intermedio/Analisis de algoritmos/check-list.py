def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in range(len(list_a)):
        for element_b in range(len(list_b)):
            if list_a[element_a] == list_b[element_b]:
                return list_a[element_a]

    return False


list_a = [1, 2, 3, 4]


list_b = [5, 6, 3, 8]

print("Elementos que son iguales:", check_if_lists_have_an_equal(list_a, list_b))
