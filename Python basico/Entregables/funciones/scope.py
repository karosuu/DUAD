num = [5, 6]


def numbers_addition(numbered_list):
    total_sum = 0

    for number in numbered_list:
        total_sum += number

    return total_sum


# Sin Global
def change_value_without_global():
    num = [26, 68]
    return num


def change_value():
    global num
    num = [25, 65]
    return num


def main():

    # Sin global
    print("\n--Sin Global--")

    print(f"Valor de num antes: {num}")

    new_values = change_value_without_global()

    print(f"Valor retornado por la funcion: {new_values}")
    print(f"Valor de num despues: {num}")

    # Observación:
    # Aunque dentro de la funcion se creo num = [25, 65],
    # esa variable es LOCAL y no modifica la variable global.
    # Por eso num sigue siendo [5, 6].

    # Con variable global
    print("\n--Con Global--")


    print(f"Valor de num antes: {num}")

    new_values = change_value()
    print(f"Nuevo valor de retornado: {new_values}")

    print(f"Valor de num después de la función: {num}")
 
# Observación:
# Al utilizar global num, Python utiliza la variable global
# y permite modificar su valor.


if __name__ == "__main__": 
    main()
