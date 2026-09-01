import json


def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def pokemon_type(data):
    poke_type = {}

    for pokemon in data:

        if pokemon["type"] not in poke_type:
            poke_type[pokemon["type"]] = []
        poke_type[pokemon["type"]].append(pokemon["level"])

    return poke_type


def main():
    filepath = "pokemon.json"
    data = read_json(filepath)
    poke_type = pokemon_type(data)

    for pokemon_type_name, levels in poke_type.items():
        average = sum(levels) / len(levels)

        print(f"Tipo: {pokemon_type_name}  Promedio de nivel: {average:.1f}")


if __name__ == "__main__":
    main()
