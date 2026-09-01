import csv

game_file = "../videojuegos.csv"


print("----Ejericio #3----")


def read_file():
    with open(game_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        games = list(reader)

    return games


# Crea un diccionario, recorre los generos
# y auemnta la cuenta si no existe en el diccionatrio
def search_genre(reader):
    genre_dic = {}
    for game in reader:
        if game["Genero"] in genre_dic:
            genre_dic[game["Genero"]] += 1
        else:
            genre_dic[game["Genero"]] = 1
# Imprime el los datos del diccionaro sewparados por coma
# Al ser un diccionarion se necesita el metodo items
    for genre, count in genre_dic.items():
        print(f"{genre}: {count}")


games = read_file()
search_genre(games)
