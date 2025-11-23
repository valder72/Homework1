def unique_words():
    t = input("Введіть речення: ")
    words = t.replace(",", " ").replace(".", " ").split()
    unique_words = set()
    for word in words:
        unique_words.add(word.lower())
    print(f"Кількість унікальних слів(loop): {len(unique_words)}")
    unique_words = set([w.lower() for w in t.replace(",", " ").replace(".", " ").split()])
    print(f"Кількість унікальних слів(list comprehension): {len(unique_words)}")
unique_words()
