import json
import time

def get_info():
    while True:
        print("""\nWhat would you like to do?
        1.Get info about total amount of money you earn.
        2.Get more detailed info about money you earn(year/month/day).""")
        try:
            choice = int(input("Enter your choice (1 or 2): ").strip())
            if choice == 1:
                with open("per_day.json", "r") as f:
                    data = json.load(f)
                    print(f"Total earnings: ${data["total"]}")
                time.sleep(2)
                print("Going back to main menu...")
                time.sleep(1)
                print("Welcome back")
                continue
            elif choice == 2:
                with open("per_day.json", "r") as f:
                    data = json.load(f)
                years = [year for year in data if year != "total"]
                print("Choose a year:")
                for i, year in enumerate(years, 1):
                    print(f"{i}. {year}")
                print("If you want to start again, enter '9999'")
                err = 0
                while True:
                    try:
                        y_choice = int(input("Enter year number: ").strip())
                        if y_choice == 9999:
                            err = 5
                            print("Going back to main menu...")
                            time.sleep(1)
                            print("Welcome back")
                            break
                        elif y_choice not in range(1, len(years)+1):
                            err += 1
                            print("Invalid year selection.")
                            if err == 5:
                                print("Invalid year selection.")
                                break

                            continue
                        year_selected = years[y_choice - 1]
                        break
                    except (ValueError, IndexError):
                        print("Invalid year selection.")
                        err += 1
                        if err == 5:
                            break
                if err == 5:
                    time.sleep(1)
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                print(f"Earnings in {year_selected}: ${data[year_selected]["total_for_year"]}")
                view_month = input("Would you like to check by month? (y/n): ").strip().lower()
                if view_month not in ("y", "yes"):
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                months = [m for m in data[year_selected] if m != "total_for_year"]
                print("Choose a month:")
                for i, month in enumerate(months, 1):
                    print(f"{i}. {month}")
                print("If you want to go back print '9999'")
                err = 0
                while True:
                    try:
                        m_choice = int(input("Enter year number: ").strip())
                        if m_choice == 9999:
                            err = 5
                            print("Going back to main menu...")
                            time.sleep(1)
                            print("Welcome back")
                            break
                        elif m_choice not in range(1, len(months)+1):
                            err += 1
                            print("Invalid year selection.")
                            err += 1
                            print("Invalid year selection.")
                            if err == 5:
                                print("Invalid year selection.")
                                break
                            continue
                        month_selected = months[m_choice - 1]
                        break
                    except (ValueError, IndexError):
                        print("Invalid year selection.")
                        err += 1
                        if err == 5:
                            break
                if err == 5:
                    time.sleep(1)
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                print(f"Earnings in {month_selected}: ${data[year_selected][month_selected]["total_for_month"]}")
                view_day = input("Would you like to check by day? (y/n): ").strip().lower()
                if view_day not in ("y", "yes"):
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                days = [d for d in data[year_selected][month_selected] if d != "total_for_month"]
                print("Choose a day:")
                for i, day in enumerate(days, 1):
                    print(f"{i}. {day}")
                err = 0
                while True:
                    try:
                        d_choice = int(input("Enter year number: ").strip())
                        if d_choice == 9999:
                            err = 5
                            print("Going back to main menu...")
                            time.sleep(1)
                            print("Welcome back")
                            break
                        elif d_choice not in range(1, len(days)+1):
                            err += 1
                            print("Invalid year selection.")
                            if err == 5:
                                print("Invalid year selection.")
                                break
                            continue
                        day_selected = days[d_choice - 1]
                        break
                    except (ValueError, IndexError):
                        print("Invalid year selection.")
                        err += 1
                        if err == 5:
                            break
                if err == 5:
                    time.sleep(1)
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                amount = data[year_selected][month_selected][day_selected]
                print(f"Earnings on {day_selected}: ${amount}")
                time.sleep(2)
                print("Going back to main menu...")
                time.sleep(1)
                print("Welcome back")
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    print("Welcome to COFFEE MACHINE INFO")
    get_info()