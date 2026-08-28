import json




def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def add_pokemon(data):

    pokemon_name = input("\nIngrese el nombre del Pokemon: ")
    pokemon_type = input("\nIngrese el tipo del Pokemon: ")
    pokemon_lvl = int(input("\nIngrese el nivel del Pokemon: "))
    pokemon_weight = float(input("\nIngrese el peso del Pokemonen Kg: "))
    pokemon_shine = int(input("\nIngresa 1 si tiene brillo o 0 si no tiene: "))
    
    while pokemon_shine != 1 and pokemon_shine != 0:
        pokemon_shine = int(input("\nIngresa 1 si tiene brillo o 0 si no tiene: "))
    shine_results = bool(pokemon_shine)
    pokemon_item = input("\nIngrese el objeto del Pokemon: ")

    skills_quantity = int(input("\nIngrese las cantidad de  habilidades del Pokemon: "))
    pokemon_skills = []
    for skill in range(skills_quantity):
        pokemon_skill = input("\nIngrese el nombre de la habilidad: ")

        pokemon_skills.append(pokemon_skill)

    pokemon_hp = int(input("\nIngrese el HP del Pokemon: "))
    pokemon_attack = int(input("\nIngrese el ataque del Pokemon: "))
    pokemon_defense = int(input("\nIngrese la defensa del Pokemon: "))
    pokemon_sp_attack = int(input("\nIngrese el ataque SP del Pokemon: "))
    pokemon_sp_defense = int(input("\nIngrese la defensa SP del Pokemon: "))
    pokemon_speed = int(input("\nIngrese la velocidad del Pokemon: "))

    pokemon_stats = {
        "hp": pokemon_hp,
        "attack": pokemon_attack,
        "defense": pokemon_defense,
        "sp_attack": pokemon_sp_attack,
        "sp_defense": pokemon_sp_defense,
        "speed": pokemon_speed,
    }

    new_pokemon = {
        "name": pokemon_name,
        "type": pokemon_type,
        "level": pokemon_lvl,
        "weight_kg": pokemon_weight,
        "is_shiny": shine_results,
        "held_item": pokemon_item,
        "skills": pokemon_skills,
        "stats": pokemon_stats,
    }

    data.append(new_pokemon)


def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    filepath = "../pokemon.json"
    data = read_json(filepath)
    add_pokemon(data)
    save_json(data, filepath)


if __name__ == "__main__":
    main()
