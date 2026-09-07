import csv


# Crea los encabezadp de la primera fila como una lista
# Recorre estudiantes y los agrega cada uno a una fila
def export_csv(students):
    with open("Archivo_de_estudiantes.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Nombre", "Seccion", "Español", "Ingles", "Sociales", "Ciencias"]
        )
        for student in students:
            writer.writerow(
                [
                    student["name"],
                    student["section"],
                    student["spanish"],
                    student["english"],
                    student["social"],
                    student["science"],
                ]
            )

        print("El archivo fue guarado correctaente")


def import_csv(filepath):
    students = []
    try:
        with open (filepath, 'r', encoding="utf-8" ) as file:
            reader = csv.DictReader(file)
            for student in reader:
                student["spanish"] = float(student["spanish"])
                student["english"] = float(student["english"])
                student["social"] = float(student["social"])
                student["science"] = float(student["science"])
                students.append(student)
    except FileNotFoundError:
        print(f"El archivo no existe {FileNotFoundError}")
            
    return students