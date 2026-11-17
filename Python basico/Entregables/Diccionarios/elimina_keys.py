print("----Elimina key de una diccionario----")
print()

list_of_keys = ["access_level", "age"]

employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

print("Este es el diccionario original")
print(employee)

for key in list_of_keys:
    if key in employee:
        del employee[key]

print()
print("Este es el diccionario luego de remover las claves: ")
print(employee)
