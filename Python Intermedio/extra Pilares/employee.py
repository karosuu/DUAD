class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("El salario no puede ser menor a 0 .")

        self._salary = new_salary

    def promote(self, percentage):

        salary_percentage = self._salary * percentage

        new_salary = salary_percentage + self._salary

        self.salary = new_salary


try:
    employee = Employee("Ana", 2000)
except ValueError as error:
    print(f"Error: {error} ")

employee.promote(0.1)  # +10%

print(f"Empleado: {employee.name}")
print(f"Salario: {employee.salary}")
