def longest_word(words):
    c=0
    word=""
    for w in words:
        if len(w)>c:
            c=len(w)
            word = w
    return word
def task():
    text = input("Введіть слова через пробіл: ")
    words = text.split()
    result = longest_word(words)
    print(f"The longest word is: {result}")
task()