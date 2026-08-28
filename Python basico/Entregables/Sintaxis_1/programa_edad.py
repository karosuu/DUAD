#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, 
# adolescente, adulto joven, adulto, o adulto mayor
print("----Clasificador de Edad----")
name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))
if age < 2:
    category = "Bebé"
    message = "¡Eres un bebé!"
elif age > 2 and age < 12:
    category = "Niño"     
    message = "¡Eres un niño!"  
elif age >= 12 and age < 14:
    category = "Preadolescente"
    message = "¡Eres un preadolescente!"
elif age >= 14 and age < 18:
    category = "Adolescente"
    message = "¡Eres un adolescente!"
elif age >= 18 and age < 30:
    category = "Adulto Joven"
    message = "¡Eres un adulto joven!" 
elif age >= 30 and age < 60:
    category = "Adulto"
    message = "¡Eres un adulto!"
else:
    category = "Adulto Mayor"
    message = "¡Eres un adulto mayor!"
print(f"{name} {last_name}, tu categoría es: {category}. {message}")

