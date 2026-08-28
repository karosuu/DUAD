print("----Convierte lista a entero----")


def convert_to_integer(items):
    for value in list:
        try:
            number = int(value)
            print(f"{value} convertido a {number}")
        except ValueError:
            print(f"\nNo se puede convertir el elemento: {value}")


result = input("Ingrese los valores separados por espacio: ")

my_list = result.split()


convert_to_integer(my_list)
