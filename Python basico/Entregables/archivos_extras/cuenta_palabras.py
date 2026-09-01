from pathlib import Path

# lee el archivo original lina por linea
def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read()

    return lines

def counting_words(path):
    count_words = read_file(path)
    words = count_words.split()
    print("\nPalabras encontradas:")
    print(words)
    
    total = len(words)
    
    return total

folder = Path(__file__).parent

input_file = folder / "../palabras.txt"

words_total = counting_words(input_file)
print(f"Este archivo contiene {words_total} palabras\n")