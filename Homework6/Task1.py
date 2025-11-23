"""Task 1 — Temperature Converter

Goal: Understand why using functions saves effort and errors.

You need to convert a large list of temperature readings between Celsius and Fahrenheit.

Temperatures (in °C): [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]
Step 1. (Naive version)

Write plain code (no functions) that converts each Celsius value to Fahrenheit and prints results in a table like:

Celsius | Fahrenheit
------- | -----------
-10     | 14.0
-5      | 23.0
...

Step 2. (Refactored version)

Now create two functions:

def c_to_f(celsius):
    ...

def f_to_c(fahrenheit):
    ...

Use a for loop with your list and print the table again. Finally, show how easily you can reverse the conversion (F→C) for the same list by just changing the function call."""

"""#Step 1:

temperature_c = [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]
print("Celsius | Fahrenheit \n------- | ----------")
for cel in temperature_c:
    far = (cel * 9 / 5) + 32
    print(f"{cel:<7} | {far:<10.1f}")"""
# Step 2:
print("Celsius | Fahrenheit \n------- | ----------")
def c_to_f(celsius):
    fahrenheit = (celsius * 5/9) + 32
    print(f"{celsius:<7} | {fahrenheit:<10.1f}")

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{celsius:<7.1f} | {fahrenheit:<10}")

temperature = [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]

for cel in temperature:
    c_to_f(cel)
