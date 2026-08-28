from pathlib import Path


def read_file_by_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return lines


def upper_cases_word(path):
    words = read_file_by_lines(path)
    for i in range(len(words)):
        words[i] = words[i].upper()
    return words


def all_upper_words(path, words):
    with open(path, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word)


folder = Path(__file__).parent

input_file = folder / "minusculas.txt"
output_file = folder / "mayusculas.txt"

new_text_file = upper_cases_word(input_file)
all_upper_words(output_file, new_text_file)