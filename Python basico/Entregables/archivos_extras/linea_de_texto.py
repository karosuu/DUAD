from pathlib import Path


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text_file = file.read()

        return text_file


def get_text():
    text_line = input("Introduzca el texto: ")

    return text_line

def add_text(path, text_line):
    with open(path, "a", encoding="utf-8") as file:
        file.write("text_line \n")
        return text_line



folder = Path(__file__).parent

input_file = folder / "palabras.txt"

new_line = get_text()
new_append_text = add_text(input_file, new_line)