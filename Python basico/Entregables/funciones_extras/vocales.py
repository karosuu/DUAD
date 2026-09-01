def find_vowels(string, vowels):
    counter = 0
    for letter in string.lower():
        if letter in vowels:
            counter += 1

    return counter


print("----Cuentas las vocales de una cadena----")
print()
string = input("Ingresa un texto: ")
vowels = "aeiou"


total = find_vowels(string, vowels)

print(f"Hay {total} vocales en esta cadena.")
