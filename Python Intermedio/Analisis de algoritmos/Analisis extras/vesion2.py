# Complejidad temporal: O(1)
# Utiliza una fórmula matemática que realiza una cantidad constante
# de operaciones, independientemente del valor de n.

# Complejidad espacial: O(1)
# No crea estructuras adicionales ni utiliza memoria proporcional
# al tamaño de la entrada.


def add_formula(n):
    return n * (n + 1) // 2

list_to_sum = [1, 2, 3, 4, 5, 7]
total_sum = add_formula(len(list_to_sum))
print(f"La suma de los primeros {len(list_to_sum)} números es: {total_sum}")