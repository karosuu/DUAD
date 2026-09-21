class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science


def add_students(students, students_quantity):
    for student_index in range(students_quantity):
        student_name = input("Ingrese el nombre del estudiante: ")
        student_section = input("Ingrese la seccion del estudiante: ")
        spanish_grade = get_valid_grade("Español")
        english_grade = get_valid_grade("Ingles")
        social_grade = get_valid_grade("Sociales")
        science_grade = get_valid_grade("Ciencia")

        student = Student(
            student_name,
            student_section,
            spanish_grade,
            english_grade,
            social_grade,
            science_grade,
        )

        students.append(student)


def show_all_students(students):
    if not students:
        print("No hay estudiantes registrados: ")
        return

    for student in students:
        print("------------------")
        print(f"Nombre: {student.name}")
        print(f"Seccion: {student.section}")
        print(f"Español: {student.spanish}")
        print(f"Ingles: {student.english}")
        print(f"Sociales {student.social}")
        print(f"Ciencias: {student.science}")
        print("------------------")


def top_three_students(students):
    for student in students:

        grade_average = calculate_average(student)
        student.average = grade_average

    sorted_students = sorted(students, key=lambda x: x.average, reverse=True)

    top_3 = sorted_students[:3]

    print("Los estudiantes top 3 son:")

    for student in top_3:
        print("------------------")
        print(f"Nombre: {student.name} ")
        print(f"Seccion: {student.section}")
        print(f"Promedio: {student.average} ")
        print("------------------")


def general_average(students):
    total_average = 0

    if not students:
        print("No hay estudiantes registrados")
        return

    for student in students:
        grade_average = calculate_average(student)
        total_average += grade_average

    average = total_average / len(students)

    print(f"El promedio general de estudiantes es: {average}")


def calculate_average(student):

    grades = [
        student.spanish,
        student.english,
        student.social,
        student.science,
    ]

    grade_average = sum(grades) / len(grades)

    return grade_average


def delete_student(students):
    student_name = input("Ingrese el nombre del estudiante que desea eliminar: ")
    student_section = input("Ingrese la seccion del estudiante: ")

    found = False

    # Busca el estudinate en el diccionario studdent de la lista students
    for student in students:
        if student_name == student.name and student_section == student.section:

            while True:
                confirmation = input(
                    "Esta seguro que desea eliminar al estudiante? (s/n): "
                ).lower()

                if not (confirmation == "s" or confirmation == "n"):
                    print(
                        "Respuesta no valida. Ingrese s para confirmar o n para cancelar."
                    )
                else:
                    break

            found = True
            # Elimina al diccionaro student que concuerde            if confirmation == "s":
            if confirmation == "s":
                students.remove(student)
                print("El estudiante fue eliminado correctamente")
                return

            if confirmation == "n":
                print("Eliminacion cancelada")
                return
    if not found:
        print("El estudiante no fue encontrado")


def show_failed_students(students):
    found = False
    for student in students:
        if (
            student.spanish < 60
            or student.english < 60
            or student.social < 60
            or student.science < 60
        ):
            found = True
            print(f"\nNombre {student.name} Seccion: {student.section}")

            if student.spanish < 60:
                print(f"Español: {student.spanish}")

            if student.english < 60:
                print(f"Ingles: {student.english}")

            if student.social < 60:
                print(f"Sociales: {student.social}")

            if student.science < 60:
                print(f"Ciencias: {student.science}")

    if not found:
        print("No hay estudiantes reprobados")
