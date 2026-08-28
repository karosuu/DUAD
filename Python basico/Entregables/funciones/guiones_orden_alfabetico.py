def alphabetic_order(text):
    words = text.split("-")
    words.sort()

    return "-".join(words)


clean_text = alphabetic_order("python-variable-funcion-computadora-monitor")
print(clean_text)
