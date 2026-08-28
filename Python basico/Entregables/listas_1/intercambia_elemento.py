print("-----Intercambiar elementos de una lista-----")

my_list = ['hola', 'soy', 'un', 'string']
print(f"Lista original: {my_list}")

print()
print("Intercambiando el primer elemento con el cuarto elemento...")
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)