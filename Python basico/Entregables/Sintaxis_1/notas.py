

counter = 1
approved_grades = 0
desapproved_grades = 0
average_passed_grades = 0
average_desapproved_grades = 0
total_average_grades = 0

total_grades = int(input("Cuantas notas desea ingresar: "))
while counter <= total_grades:
    print("Ingrese la nota numero", counter)
   
    actual_grade = float(input("Ingrese la nota actual: "))
    if actual_grade < 70:
        desapproved_grades = desapproved_grades + 1
        average_desapproved_grades = average_desapproved_grades + actual_grade
        counter = counter + 1
    else:
        approved_grades = approved_grades + 1
        average_passed_grades = average_passed_grades + actual_grade
        counter = counter + 1
    total_average_grades = total_average_grades + (actual_grade / total_grades)
    
if  desapproved_grades > 0:
    average_desapproved_grades = average_desapproved_grades / desapproved_grades

if  approved_grades > 0:
    average_passed_grades = average_passed_grades / approved_grades



print(f"El estudiante tiene esta cantidad de nota aprobadas: {approved_grades}")
print(f"El promedio de las notas aprobadas es: {average_passed_grades}")
print(f"El estudiante tiene esta cantidad de nota desaprobadas: {desapproved_grades}")
print(f"El promedio de las notas desaprobadas es: {average_desapproved_grades}")
print(f"El promedio total de las notas es: {total_average_grades}")


