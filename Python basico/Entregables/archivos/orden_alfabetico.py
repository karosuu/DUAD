# lee el archivo original lina por linea
def read_file_by_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return lines

# ordena las canciones por order alfabetico
def songs_in_alphabetic_order(path):
    songs = read_file_by_lines(path)
    songs.sort()
    return songs


# Crea el nuevo archivo y escribe las canciones.
def write_new_songs(path, songs):
    with open(path, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song)


ordered_songs = songs_in_alphabetic_order('canciones.txt')
write_new_songs("canciones ordenada.txt", ordered_songs)
