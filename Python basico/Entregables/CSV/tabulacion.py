import csv


def get_games():
    games_quantity = int(input("Cuantos video juegos quiere ingresar: "))
    games_list = []
    count = 1
    while count <= games_quantity:
        games_name = input(f"\nIngrese el nombre del juego {count}: ")
        games_genre = input("\nIngrese el genero del juego: ")
        games_company = input("\nIngrese el desarrollador del juego: ")
        games_classification = input("\nIngrese la clasificacion ESRB del juego: ")
        count += 1
        games_list.append(
            {
                "Name": games_name,
                "Genre": games_genre,
                "Developer": games_company,
                "Clasification": games_classification,
            }
        )
    return games_list


def save_games(file_path, data):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        headers = data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=headers,  delimiter='\t')
    
        writer.writeheader()
        
        writer.writerows(data)


games_file = get_games()
save_games("videojuegostabulado.csv", games_file)
