#Cree un decorador @repeat_twice que haga
# que la función decorada se ejecute dos veces seguidas, con los mismos argumentos

def repeat_twice(func):
    def wrapper(*args, **kwargs):
        
        func (*args, **kwargs) # Primera ejecución
        
        return func(*args, **kwargs) # Segunda ejecución y retorno del valor
    
    return wrapper
        
@repeat_twice
def print_text(name):
        
        print("Hola", name)
        
print_text("Jeanca")
