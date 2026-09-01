def append_to_file(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file:
        # Añadimos un salto de línea antes del nuevo texto para no pegarlo al anterior
        file.write("\n" + extra_text)

additional_text = "Hechas, pues, estas prevenciones, no quiso aguardar más tiempo a poner en efeto su pensamiento..."

append_to_file('quijote_capitulo2.txt', additional_text)