def print_decorator(func):
    def wrapper(*args, **kwargs):
        
        print("Parámetro:", args)
        
        result = func(*args, **kwargs)

        print("Retorno:", result)

        return result

    return wrapper


@print_decorator
def suma(a, b):
    return a + b


result = suma(10, 5)

print("Resultado final:", result)
