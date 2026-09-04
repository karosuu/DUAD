students = []


# Solicitamos la cantidad de estudinates y debe ser mayor  a 0
def get_students_quantity():
    while True:
        try:
            students_quantity = int(input("Cuantos estudiantes desea ingresar"))
        except ValueError as error:
            print("Ingrese un valor correcto")
            continue

        if students_quantity > 0:
            return students_quantity

        else:
            print("Debe ingresar al menos un estudiante")


# Se solicitan los datos del estudiantes y se crea el diccionario
# para guardar los valores
def add_students(students_quantity):
    for students_index in range(students_quantity):
        students_name = input("Ingrese el nombre del estudiante: \n")
        students_section = input("Ingrese la seccion del estudiante: ")
        spanish_grade = get_valid_grade("Español")
        english_grade = get_valid_grade("Ingles")
        social_grade = get_valid_grade("Sociales")
        science_grade = get_valid_grade("Ciencia")

        stundents_dict = {
            "name": students_name,
            "section": students_section,
            "spanish": spanish_grade,
            "english": english_grade,
            "social": social_grade,
            "science": science_grade,
        }

        students.append(stundents_dict)


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
def show_all_students():
    for student in students:
        print("------------------")
        print(f"Nombre: {student['name']}")
        print(f"Seccion: {student['section']}")
        print(f"Español: {student['spanish']}")
        print(f"Ingles: {student['english']}")
        print(f"Sociales {student['social']}")
        print(f"Ciencias: {student['science']}")
        print("------------------")


# Calcula el top 3 de estudiants por su average de notas
def top_three_students():
    for student in students:
        calculate_average(student)

        grade_average = calculate_average(student)
        student["average"] = grade_average
    students.sort(key=lambda x: x["average"], reverse=True)

    top_3 = students[:3]

    print("Los estudiantes top 3 son:")

    for student in top_3:
        print("------------------")
        print(f"Nombre: {student['name']} ")
        print(f"Seccion: {student['section']}")
        print(f"Promedio: {student['average']} ")
        print("------------------")


# Se calcula el promedio general
def general_average():
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
        student["spanish"],
        student["english"],
        student["social"],
        student["science"],
    ]

    grade_average = sum(grades) / len(grades)

    return grade_average
