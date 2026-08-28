def character_counter(text, character):
    counter = 0
    for letter in text:
        if letter == character:
            counter += 1
    return counter


print("----Busca un caracter especifico----")
print()
text = input(" ingrese una palabra: ")
print()
character = input("Ingrese el caracter que desea buscar: ")


result = character_counter(text, character)
print(f"Seha encontrado {result} el caracter")
