import json


def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def print_pokemon_info(data):
    for pokemon in data:

        print(
            f"\nNombre: {pokemon['name']}\n"
            f"Tipo: {pokemon['type']}\n"
            f"Nivel: {pokemon['level']}\n"
            f"Peso: {pokemon['weight_kg']}\n"
            f"Brillo: {pokemon['is_shiny']}\n"
            f"Accesorio: {pokemon['held_item']}\n"
            f"Habilidades: {', '.join(pokemon['skills'])}"
        )
        for stats, count in pokemon["stats"].items():
            print(f"Estadisticas {stats}: {count}")


def main():
    filepath = "pokemon.json"
    data = read_json(filepath)
    print_pokemon_info(data)


if __name__ == "__main__":
    main()
