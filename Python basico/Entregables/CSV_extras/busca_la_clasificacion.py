import csv
game_file = "../videojuegos.csv"

#este es elejercicio 1
print("----Ejericio #2----")
def read_file():
    with open(game_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        games = list(reader)
        
    return games
        
def search_classification(reader):        
        search_text = input("\nIngrese la clasifacion a buscar: ").upper()
        found = False
        for classification in reader:
            if search_text == classification["Clasificacion"].upper():
                found = True
                print(
                    f"Estos son los juegos Clasificacion:\n"                    
                    f"{classification['Nombre']}\n" 
                    f"{classification['Genero']}\n" 
                    f"{classification['Desarrollador']}\n" 
                    f"{classification['Clasificacion']}\n" 
                    )
        if not found:
            print("No se encontro ningun juego con esa clasificacion")    
                
games = read_file()
search_classification(games)