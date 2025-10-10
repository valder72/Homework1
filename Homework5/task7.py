"""
🚗 TASK 7 — Group Car Colors by Brand
Topic: list of tuples → dict of lists

Cars: [("BMW","black"), ("Audi","red"), ("BMW","white"), ("Audi","blue")]
Build a dictionary where key is the brand and value is a list of colors for that brand.

"""
# Starter:
cars = [("BMW","black"), ("Audi","red"), ("BMW","white"), ("Audi","blue")]
# TODO: build brand -> list_of_colors dict and print it
brand = {}
for car in cars:
    brand[car[0]] = brand.get(car[0], []) + [car[1]]
print(brand)
