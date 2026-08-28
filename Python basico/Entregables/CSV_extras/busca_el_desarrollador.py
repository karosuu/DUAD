import csv

print("----Ejericio #4----")

game_file = "../videojuegos.csv"


def read_file():
    with open(game_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        games = list(reader)

    return games


# Busca el desarrollador que pide el usuario
# Crea una lista vacia y los guarada
def search_developer(reader):
    search_text = input("\nIngrese el desarrollador que busca: ").upper()
    games_found = []
    found = False
    for game in reader: #recorre juegos y agrega a la lista los que coinciden con el desarroolador
        if search_text == game["Desarrollador"].upper():
            games_found.append(game)
            found = True
    for game in games_found: #Recorre los juesgos encontrados
        print(
            f"\nEstos son los del desarrollador {game['Desarrollador']}:\n"
            f"{game['Nombre']}\n"
            f"{game['Genero']}\n"
            f"{game['Desarrollador']}\n"
            f"{game['Clasificacion']}"
        )
        print("--------------")
    if not found:
        print("No se encontro ningun juego con ese desarrollador: ")


games = read_file()
search_developer(games)
