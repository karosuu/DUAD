print("--Este programa crea un diccionario con dos listas una para keys y otra para values--")
print()

values = []
keys = []

quantity = int(input("Ingrese la cantidad de valores: "))

print("Ingrese las Keys")
for i in range (quantity):
    key = input(f"Key {i + 1}: ")
    keys.append(key)
    
    
print()

print("Ingrese los Values")
for i in range(quantity):
    value = input(f"Value {i + 1}: ")
    values.append(value)

dictionary = { }

for i in range(quantity):    
    dictionary[keys[i]] = values[i]   

print()
print("---Informacion de listas----")
print(dictionary)
    