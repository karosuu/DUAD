count = 1
print("-----Tabla de multiplicar-----")
print()
num = int(input("Ingrese un numero del 1 al 10: "))
while (num < 1 or num > 10):
   if (num > 10):
      print("No puede ingresar un numero mayor a 10")

   else:
      print("No puede ingresar un numero menor a 1")
   num =int(input("Ingrese otro numero: "))
for i in range (1, 13):
   print(f"{num} x {i} = {num*i}")