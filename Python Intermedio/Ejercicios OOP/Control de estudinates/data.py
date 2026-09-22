import csv
from student import Student


# Crea los encabezadp de la primera fila como una lista
# Recorre estudiantes y los agrega cada uno a una fila
def export_csv(students):
    with open("Archivo_de_estudiantes.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "section", "spanish", "english", "social", "science"])
        for student in students:
            writer.writerow(
                (
                    student.name,
                    student.section,
                    student.spanish,
                    student.english,
                    student.social,
                    student.science,
                )
            )
        return True


# valida si el archivo a importar no existe con el try y exception
def import_csv(filepath):
    students = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for student in reader:
                student["spanish"] = float(student["spanish"])
                student["english"] = float(student["english"])
                student["social"] = float(student["social"])
                student["science"] = float(student["science"])

                student = Student(
                    student["name"],
                    student["section"],
                    student["spanish"],
                    student["english"],
                    student["social"],
                    student["science"],
                )

                students.append(student)
    except FileNotFoundError:
        pass

    return students
