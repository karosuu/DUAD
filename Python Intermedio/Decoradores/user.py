from datetime import datetime, date


class User:
    def __init__(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def age(self):

        date_now = datetime.now()
        actual_year = date_now.year
        actual_month = date_now.month
        actual_day = date_now.day

        birth_year = self._date_of_birth.year
        birth_month = self._date_of_birth.month
        birth_day = self._date_of_birth.day

        calculate_age = actual_year - birth_year

        if actual_month < birth_month:
            calculate_age = calculate_age - 1

        elif actual_month == birth_month and actual_day < birth_day:
            calculate_age = calculate_age - 1

        return calculate_age
    
# Excepción personalizada
class UserNotAdultError(Exception):
    pass

# Decorador
def adult_only(func):
    def wrapper(user):

        if user.age < 18:
            raise UserNotAdultError("El usuario debe ser mayor de edad.")

        return func(user)

    return wrapper

# Función protegida por el decorador
@adult_only
def add(user):
    return f"Usuario autorizado. Edad: {user.age}"


# Usuario adulto
user_adult = User(date(2000, 5, 15))
try:
    print(add(user_adult))
except UserNotAdultError as error:
    print(f"Error: {error}")

# Usuario menor
# user_minor = User(date(2015, 5, 15))

# try:
#     print(add(user_minor))
# except UserNotAdultError as error:
#     print(f"Error: {error}")
