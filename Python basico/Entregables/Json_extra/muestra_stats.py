import json


def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def pokemon_stats(data):

    for pokemon in data:

        print(f"\nNombre: {pokemon['name']}")

        for stats, count in pokemon["stats"].items():
            print(f"Estadisticas {stats}: {count}")


def main():
    print("\nMuestra las estadisticas de los pokemon en el archivo json: ")
    filepath = "pokemon.json"
    stats_search = read_json(filepath)
    pokemon_stats(stats_search)


if __name__ == "__main__":
    main()
