import random

secret_number = random.randint(1, 10)
print("----Adivina el número secreto----")
user_number = int(input("Adivina el número secreto (entre 1 y 10): "))

while user_number != secret_number:
    print("¡Número incorrecto! Intenta de nuevo.")
    user_number = int(input("Ingrese otro número: "))  

print(f"¡Felicidades! Adivinaste el número secreto: {secret_number}")
