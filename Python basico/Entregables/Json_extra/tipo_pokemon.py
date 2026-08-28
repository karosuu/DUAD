import json


def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def pokemon_type(data, search_pokemon_type):

    found = False
    for poke_type in data:
        if search_pokemon_type == poke_type["type"].upper():
            found = True
            print(
                f"Estos son los pokemon tipo {poke_type['type']}:  {poke_type['name']}"
            )
    if not found:
        print("No se encontro ningun pokemon de ese tipo")


def main():
    filepath = "pokemon.json"
    search_pokemon_type = input("\nIngrese el typo de pokemon a buscar: ").upper()
    type_search = read_json(filepath)
    pokemon_type(type_search, search_pokemon_type)


if __name__ == "__main__":
    main()
