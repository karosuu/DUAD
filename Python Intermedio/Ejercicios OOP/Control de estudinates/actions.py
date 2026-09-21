from student import Student


# Solicitamos la cantidad de estudinates y debe ser mayor  a 0
def get_students_quantity():
    while True:
        try:
            students_quantity = int(input("Cuantos estudiantes desea ingresar: "))
        except ValueError as error:
            print("Ingrese un valor correcto")
            continue

        if students_quantity > 0:
            return students_quantity

        else:
            print("Debe ingresar al menos un estudiante")


# Se solicitan los datos del estudiantes y se crea el diccionario
# para guardar los valores
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


# Se valida que la nota se mayor a 0 y menor que 100
def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Ingrese una nota valida para {subject}: "))
        except ValueError:
            print("Ingrese un numero valido")
            continue

        if 0 <= grade <= 100:
            return grade
        else:
            print("La nota debe estar en 0 y 100.")


# Muestra todos los estudiantes con sus datos
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


# Calcula el top 3 de estudiants por su average de notas
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


# Se calcula el promedio general
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


# Se calcula el average indivula de cada estudiante
# Se reutilizqa en general_average y en top_three_students
def calculate_average(student):

    grades = [
        student.spanish,
        student.english,
        student.social,
        student.science,
    ]

    grade_average = sum(grades) / len(grades)

    return grade_average


# Pide el nombre y seccion del estudiante
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
