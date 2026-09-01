from pathlib import Path

# lee el archivo original lina por linea
def read_file_by_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return lines


# Elimina los saltos de linea
def remove_line_break(path):
    remove_lines = read_file_by_lines(path)
    for i in range(len(remove_lines)):
        remove_lines[i] = remove_lines[i].rstrip()
    return " ".join(remove_lines)


# Escribe el nuevo archivo
def new_text_no_break(path, remove_lines):
    with open(path, "w", encoding="utf-8") as file:
            file.write(remove_lines)

folder = Path(__file__).parent

input_file = folder / "linea por linea.txt"
output_file = folder / "texto sin saltos.txt"

no_lines_break = remove_line_break(input_file)
new_text_no_break(output_file, no_lines_break)