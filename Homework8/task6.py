def short_words():
    text = input("Введіть речення: ")
    upper_lc = [w.upper() for w in text.replace(",", "").replace(".", "").split() if len(w) <= 3]
    list_w = []
    for word in text.replace(",", "").replace(".", "").split():
        if len(word) <= 3:
            list_w.append(word.upper())
    print(f"Результат(loop): {list_w}")
    print(f"Результат(list comprehension): {upper_lc}")
short_words()