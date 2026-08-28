def get_name():
    while True:
        try:
            name = input("\nIngrese su nombre: ")
            if name.isdigit():
                raise ValueError(name)
            return name
        except ValueError:
            print("El nombre no puede ser un numero")
        

def get_age():
    while True:
        try:
            age = int(input("\nIngrese su edad: "))
            return age 
        except ValueError:
            print("La edad no pueden ser letras")
        

def main():
    saved_name = get_name()
    saved_age = get_age()
    
    print(f"\nHola {saved_name} Su edad es {saved_age}")

if __name__ == "__main__":
    main()