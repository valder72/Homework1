"""
Task 6 — Warehouse Stock Update 🏭

Requirements:
  - inventory = [["laptops", 15], ["keyboards", 40], ["mice", 30]]
  - A customer buys 3 keyboards
  - Use a loop to find "keyboards" and decrease quantity (not below 0)
  - Print old and new quantity

Practice: lists of lists, searching, in-place mutation

OUTPUT EXAMPLE
--------------
Inventory: [['laptops', 15], ['keyboards', 37], ['mice', 30]]
keyboards: 40 -> 37
"""

inventory = [["laptops", 15], ["keyboards", 40], ["mice", 30]]
print("(Starter) Inventory:", inventory)
# TODO: find "keyboards" row and subtract 3 (min 0), then print before/after
new_key = []
for item in inventory:
    if "keyboards" in item:
        key_bef = item[1]
        item[1] -= 3
        key_aft = item[1]
    new_key.append(item)
print("Inventory:", new_key)
print(f"keyboards: {key_bef} -> {key_aft}")