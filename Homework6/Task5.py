"""Task 5 — Calendar Helper (Advanced)

Goal: Use function composition and data structures.

Write:

    1.is_leap(year) — returns True if leap year.
    2.days_in_month(month, year) — returns number of days in that month (account for leap years).
    3.next_month(month, year) — returns (next_month, next_year) (e.g., 12→1 and increment year).

    4.month_summary(month, year) — prints:
        month name,
        days count,
        leap year info.

Ask the user for a starting month/year, and show info for the next 3 months automatically.

Example:

Enter month: 11
Enter year: 2024

November 2024 – 30 days
December 2024 – 31 days
January 2025 – 31 days (Leap Year: Yes)
"""
def is_leap(year):
    return (year % 4 == 0 and year % 100) or year % 400 == 0

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap(year):
           return 29
        else:
           return 28


def next_month(month, year):
    if month == 12:
        return 1, year + 1
    return month + 1, year

def month_summary(month, year):
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = days_in_month(month, year)
    print(f"{month_name[month-1]} {year} – {days} days", end=" ")
    if is_leap(year):
        print("(Leap Year: Yes)")
    else:
        print()


month = int(input("Enter month (1–12): "))
if month < 1 or month > 12:
    print("Please enter a valid month.")
year = int(input("Enter year: "))

for i in range(3):
    month_summary(month, year)
    month, year = next_month(month, year)

