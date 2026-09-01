def words_count(word_list, words_quantity):
    new_words = []
    for words in word_list:
        if len(words) > words_quantity:
            new_words.append(words)

    return new_words


print("----busca palabras con dada cantidad de letras----")
print()
word_list = ["cielo", "sol", "maravilloso", "día"]

words_quantity = int(input("Ingrese el numero minimo de letras: "))


filtered = words_count(word_list, words_quantity)


print(filtered)
