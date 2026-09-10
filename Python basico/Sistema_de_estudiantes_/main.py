from menu import show_menu
from actions import (
    students,
    get_students_quantity,
    add_students,
    show_all_students,
    top_three_students,
    general_average,
    delete_student,
    show_failed_students
)
from data import export_csv, import_csv


def main():
    option = 0
    while option != 7:
        option = show_menu()        

        if option == 1:
            students_quantity = get_students_quantity()
            add_students(students_quantity)

        elif option == 2:
            show_all_students()

        elif option == 3:
            top_three_students()

        elif option == 4:
            general_average()
        
        elif option == 5:
            export = export_csv(students)
            if export:
                print("El archivo fue guardado correctamente")    

        # Se limpia la lista "students " que proviene de actions.
        # agrega los datos mportados de "imported_students" a la lista de actions.py
        elif option == 6:
            imported_students = import_csv("Archivo_de_estudiantes.csv")
            if imported_students:
                students.clear()
                students.extend(imported_students)
                print("Estudiantes actualizados con exito")
            else:
                print("No hay datos que importar.")
                
        elif option == 7:
            break
        
        elif option == 8:
            delete_student(students)
        
        elif option == 9:
            show_failed_students(students)           


if __name__ == "__main__":
    main()
