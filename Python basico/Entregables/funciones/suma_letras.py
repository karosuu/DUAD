string = input("Ingrese una cadena con mayusculas y minusculas: ")
def detect_letters(letters):
    upper_count = 0
    lower_count = 0
    
    for letter in letters:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    return {"Mayusculas": upper_count, "minusculas": lower_count}

final_count = detect_letters(string)
print(final_count)