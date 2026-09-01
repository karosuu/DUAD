print("----Suma valores de una lista----")


def values_addition(list):
    addition = 0
    for value in list:
        try:
            user_float = float(value)
            addition = addition + user_float
            print(f"{user_float} Valor sumado correctamente")

        except ValueError:
            print(f"\nElemento invalido: {value}")

    return addition


list_input = input("Ingrese los valores de la lista: ")

my_list = list_input.split()

result = values_addition(my_list)
print(f"\nEl total de la suma es:  {result}")
