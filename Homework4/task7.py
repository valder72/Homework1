"""
Task 7 — ATM Cash Dispenser 🔢

Requirements:
  - bills = [100, 50, 20, 10]
  - For amount = 180, calculate greedy breakdown
  - Print like: "1x100, 1x50, 1x20, 1x10"
  - If not divisible by 10, print an error message

Practice: loops, integer division, modulo, conditional handling

OUTPUT EXAMPLE
--------------
1x100, 1x50, 1x20, 1x10
"""

amount = 180
bills = [100, 50, 20, 10]
print(f"(Starter) Amount: {amount}, Bills: {bills}")
# TODO: implement greedy breakdown and print result (or error if remainder)
for bill in bills:
    if bill <= amount:
        i = amount//bill
        amount -= i*bill
        print(f"{i}x{bill}", end=" ")
