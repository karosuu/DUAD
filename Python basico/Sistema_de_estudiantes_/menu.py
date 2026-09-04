


def show_menu():
    print("\n-----Menu del sistema de estudiantes")
    print("1. Ingresar a estudiantes")
    print("2. Ver todos los estudiantes")
    print("3. Ver Top 3")
    print("4. Ver promedio general")
    print("5. Exportar CSV")
    print("6. Importar CSV")
    print("7. Salir")
    print ("8. Eiminar estudiantes")
    print ("9. Ver estudiantes reprobados")
    
def user_menu_action():
    
    while True:
        show_menu()
        
        try:
            option = int(input("Selecciones una opcion: "))
        except ValueError as error:
            print(f"Opcion no valida {error}")
            continue
    
        if option  == 1:
           
            
                
                   
               
                
        elif option == 2:
            
        elif option == 3:
        
        
        elif option == 4:
        
        elif option == 5:
            
        elif option == 6:
        
        elif option == 7:
            break    
        
        elif option == 8:            
            
        elif option == 9:    
        
        else:
            print("Opcion no valida")    