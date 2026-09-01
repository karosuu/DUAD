def get_number():
    while True:
        try:
            num = float(input("Ingrese un numero: "))
            return num
        except ValueError:
            print("Valor no valido, intente de nuevo")


def addition(current_number, new_number):
    return current_number + new_number


def subtract(current_number, new_number):
    return current_number - new_number


def multiply(current_number, new_number):
    return current_number * new_number


def divide(current_number, new_number):
    return current_number / new_number


def show_results(previous_number, operator, new_number, current_number):
    print(f"{previous_number} {operator} {new_number} = {current_number}")


def show_menu():
    print("\n------CALCULADORA-----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")
    print("----------------------")
    print()


def main():
    current_number = get_number()

    while True:
        show_menu()

        try:
            option = int(input("Selecciona una opcion: "))
        except ValueError as error:
            print(f"Opcion no valida {error}")
            continue

        if option == 1:
            previous_number = current_number
            new_number = get_number()

            current_number = addition(current_number,new_number)

            show_results(previous_number, "+", new_number, current_number)

        elif option == 2:
            previous_number = current_number
            new_number = get_number()

            current_number = subtract(current_number, new_number)

            show_results(previous_number, "-", new_number, current_number)

        elif option == 3:
            previous_number = current_number
            new_number = get_number()

            current_number = multiply(current_number, new_number)

            show_results(previous_number, "*", new_number, current_number)

        elif option == 4:
            previous_number = current_number
            new_number = get_number()
            try:
                current_number = divide(current_number, new_number)
                show_results(previous_number, "/", new_number, current_number)

            except ZeroDivisionError:
                print("No se puede dividir entre 0")
                continue

        elif option == 5:
            current_number = 0
        elif option == 6:
            print("Usted acaba de salir de la calculadora")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()
