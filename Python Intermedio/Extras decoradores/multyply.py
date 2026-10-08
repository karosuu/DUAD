from datetime import date, datetime
from functools import wraps


def log_call(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        date = datetime.now()
        result = func(*args, **kwargs)
        print(func.__name__)
        print("Estos los argumentos:", args)
        print(f"Fecha de hoy: ", date)
        print(f"Resultado: ", result)

        return result

    return wrapper


def validate_numbers(func):

    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Alguno de los valores no es numericos: {args}")
        return func(*args, **kwargs)

    return wrapper


@log_call
@validate_numbers
def multiply(value1, value2):
    result = value1 * value2

    return result


try:
    multiply(6, "hola")

except TypeError as error:
    print(error)
