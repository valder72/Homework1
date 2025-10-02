"""
Task 3 — Class Exam Results 📊

Requirements:
  - grades = [45, 72, 88, 91, 60, 55]
  - Compute average using a loop (avoid sum())
  - Gather grades strictly above the average into a new list
  - Print the average and the list

Practice: loop aggregation, conditional filtering

OUTPUT EXAMPLE
--------------
Average: 68.50
Above average: [72, 88, 91]
"""

grades = [45, 72, 88, 91, 60, 55]
print("(Starter) Grades:", grades)
# TODO: compute average via a loop (no sum())
# TODO: build a list of grades > average
# TODO: print both
i = 0
for grade in grades:
    i += grade
i = i / len(grades)
print(f"Average: {i:.2f}")
ab_av_grade = []
for grade in grades:
    if grade > i:
        ab_av_grade.append(grade)
print("Above average:", ab_av_grade)