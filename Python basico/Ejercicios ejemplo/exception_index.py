def main():
    my_list = ["2", "Hello"]
    index_to_use = 4

    try:
        list_element_to_convert = my_list[index_to_use]
        element_to_int = int(list_element_to_convert)
        print(element_to_int)
    except IndexError as error:
        print(f"El indice a usar no existe en la lista. Error: {error}")
    except ValueError as error:
        print(f"El elemento de la lista no es un numero valido. Error: {error}")


if __name__ == "__main__":
    main()
