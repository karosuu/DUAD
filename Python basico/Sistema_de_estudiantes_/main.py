from menu import show_menu
from actions import (
    students, 
    get_students_quantity, 
    add_students, show_all_students, 
    top_three_students, 
    general_average,
    )
from data import (export_csv, import_csv)


def main():
    option = 0
    while option != 7:
        option = show_menu()
        
        if option == 5:
            export_csv(students)
        
        if option == 1:
            students_quantity = get_students_quantity()
            add_students(students_quantity)
        
        if option == 2:
            show_all_students()
            
        if option == 3:
            top_three_students()
        
        if option == 4:
            general_average()
        
        # Se limpia la lista "students " que proviene de actions.
        # agrega los datos mportados de "imported_students" a la lista de actions.py
        if option == 6:
            imported_students = import_csv("Archivo_de_estudiantes.csv")
            students.clear()
            students.extend(imported_students)



if __name__ == "__main__":
    main()

