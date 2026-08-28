
time_in_seconds = int(input("Ingrese el tiempo en segundos: "))
if time_in_seconds < 600:
    missing_seconds = 600 - time_in_seconds
    print(f"faltan {missing_seconds} segundos para completar 10 minutos.")
else:
    if time_in_seconds > 600:
        print("El tiempo ingresado es MAYOR a 10 minutos.")
    else:
        time_in_seconds == 600
        print("El tiempo ingresado es IGUAL a 10 minutos.")
