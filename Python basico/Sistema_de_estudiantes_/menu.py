def show_menu():
    print("\n-----Menu del sistema de estudiantes")
    print("1. Ingresar a estudiantes")
    print("2. Ver todos los estudiantes")
    print("3. Ver Top 3")
    print("4. Ver promedio general")
    print("5. Exportar CSV")
    print("6. Importar CSV")
    print("7. Salir")
    print ("8. Eliminar estudiantes")
    print ("9. Ver estudiantes reprobados")
    
    while True:
        try:
            option = int(input("Seleccione una opcion: "))
        except ValueError as error:
            print(f"Opcion no valida {error}")
            continue
        
        if 1 <= option <= 9:
            return option
        else:
            print("Opcion nmo valida")