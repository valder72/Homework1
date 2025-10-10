"""
📚 TASK 8 — Word Frequency
Topic: strings → list → dictionary (frequency)

Text: "hello world hello python world hello"
Count how many times each word occurs. Print the dictionary sorted by word (key).
"""
# Starter:
text = "hello world hello python world hello"
# TODO: split into words; count frequencies into dict; print in key-sorted order
text = text.split()
count = {}
for word in text:
    count[word] = count.get(word, 0) + 1
print(dict(sorted(count.items())))