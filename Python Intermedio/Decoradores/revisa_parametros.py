def only_numbers(func):
    def wrapper(*args):
        
        for arg in args:
            if not isinstance (arg,(int,float)):
                raise TypeError("Todos los parametros deben ser numeros")
        
        return func(*args)    
        
    return wrapper

@only_numbers
def add(a,b):
    return a + b

print(add(10,20))