# Complejidad temporal: O(n)
# El ciclo recorre los números desde 1 hasta n, realizando una
# operación de suma constante en cada iteración.

# Complejidad espacial: O(1)
# Utiliza únicamente variables auxiliares y no crea estructuras
# adicionales que dependan del tamaño de la entrada.

def manual_add(n):

    result = 0
    for i in range(1, n + 1):
        result += i
    return result

list_to_sum = [1, 2, 3, 4, 5, 6]
total_sum = manual_add(len(list_to_sum))
print(f"La suma de los primeros {len(list_to_sum)} números es: {total_sum}")