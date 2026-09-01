print("Lee 5 palabras y determina cuáles tiene mas de  4 letras.")

words_list = []
new_words= []

for i in range (5):
    word = input(f"Ingrese la palabra {i + 1}: ")
    words_list.append(word)    

    if len(word) > 4:
        new_words.append(word)
        
print(f"Las palabras con más de 4 letras son: {new_words}")