employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

department_employees = {}

for employee in employees:
    department = employee["department"]
    
    if department not in department_employees:
        department_employees[department] = []
    
    department_employees[department].append(employee)

for department, employees_list in department_employees.items():
    print(f"Departamento: {department}")
    for employee in employees_list:
        print(f"- {employee['name']} ({employee['email']})")