"""Task 2 — Simple Statistics (Extended)

Goal: Work with multiple cooperating functions and clean structure.

You get a list of numbers entered by the user (space-separated). Create and use four functions:

    1.get_min(numbers)
    2.get_max(numbers)
    3.get_average(numbers)
    4.get_median(numbers)

Each returns its respective value. Handle the case where the user enters no numbers or invalid input (show a friendly error).

Finally, print a short summary like:

Count: 8
Min: 1
Max: 42
Average: 13.5
Median: 10.5"""

def get_min(*numbers):
    minimum = int(numbers[0])
    for number in numbers:
        if number < minimum:
           minimum = number
    return minimum
def get_max(*numbers):
    maximum = int(numbers[0])
    for number in numbers:
        if number > maximum:
           maximum = number
    return maximum
def get_average(*numbers):
    summery = 0
    length = 0
    for number in numbers:
        summery += number
        length += 1
    return summery / length
def get_median(*numbers):
    length = 0
    for number in numbers:
        length += 1
    if length % 2 == 0:
        return (numbers[int(length / 2)] + numbers[int(length / 2) - 1]) / 2
    else:
        return numbers[int(length / 2)]

while True:
    try:
        numlist = [int(s) for s in input("Enter numbers separated by space: ").split()]
        break
    except ValueError:
        print("Please enter only numbers separated by spaces. Try again.")
count = 0
for number in numlist:
        count += 1

print(f"Count: {count}")
print(f"Min: {get_min(*numlist)}")
print(f"Max: {get_max(*numlist)}")
print(f"Average: {get_average(*numlist)}")
print(f"Median: {get_median(*numlist)}")