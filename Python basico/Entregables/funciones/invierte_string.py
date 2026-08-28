def string_revert(my_string):
    reverted_string = ""

    for i in range(len(my_string) - 1, -1, -1):
        reverted_string += my_string[i]

    return reverted_string


print("----Invierte un texto de direccion----")
print()
my_string = input("ingresge un texto: ")


result = string_revert(my_string)
print(result)
