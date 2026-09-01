import csv
game_file = "videojuegos.csv"

#este es elejercicio 1
print("----Ejericio #1----")
def read_file():
    with open(game_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for games in reader:
                print (
                    f"Nombre: { games['Nombre']}\n" 
                    f"Genero: {games['Genero']}\n" 
                    f"Desarrollador: {games['Desarrollador']}\n"
                    f"Clasificacion: {games['Clasificacion']}\n"
                    )
    print("-------------------")            
read_file()