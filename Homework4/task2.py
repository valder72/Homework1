"""
Task 2 — Gym Repetitions Counter ⏱

Requirements:
  - Set target = 12
  - Use a for-loop with range function to print: "Push-up 1 done" ... "Push-up 12 done"
  - End with "Workout complete!"

Practice: for-range, printing

OUTPUT EXAMPLE
--------------
Push-up 1 done
Push-up 2 done
...
Push-up 12 done
Workout complete!
"""

target = 12
print("(Starter) Target:", target)
# TODO: loop using range function prints "Push-up X done" for X from 1..target
# TODO: finish with "Workout complete!"
for i in range(1, target + 1):
    print(f"Push-up {i} done")
    if i == target:
        print("Workout complete!")