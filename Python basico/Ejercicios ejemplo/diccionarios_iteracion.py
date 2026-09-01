new_dicationary = {
    "name": "Juan",
    "age": 30,
    "city": "Madrid",
    "email": "juan@lyfter.com"
}

print("USando el item() para recorrer el diccionario")
for key, value in new_dicationary.items():
    print({key})
    print({value})
print()
print("Usando el keys() para recorrer el diccionario ")
for key in new_dicationary.keys():
    print({key})
print()
print("Usando el values() para recorrer el diccionario ")
for value in new_dicationary.values():
    print({value})
print()
print("Usando el get() para recorrer el diccionario ")
for key in new_dicationary.keys():
    print({new_dicationary.get(key)})   
print()
print("Agreagr un nuevo item al diccionario")
new_dicationary["phone"] = "123-456-7890"   
print(new_dicationary)
