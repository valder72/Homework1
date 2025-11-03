import json
import time
import logging
def check_res():
    with open("coffee_logs.log", "r") as res_file:
        res_file=res_file.read().split("\n")[:-1]
        for n in res_file[::-1]:
            if "Not enough resources" in n:
                return True
            elif "Resources refilled" in n:
                return True
        return False

def check_choice(y_m_d):
    err = 0
    while True:
        try:
            choice = int(input("Enter year number: ").strip())
            if choice == 9999:
                return False
            elif choice not in range(1, len(y_m_d) + 1):
                err += 1
                print("Invalid data selection.")
                if err == 5:
                    print("Invalid data selection.")
                    return False
                continue
            year_selected = y_m_d[choice - 1]
            return year_selected
        except (ValueError, IndexError):
            print("Invalid year selection.")
            err += 1
            if err == 5:
                return False
def get_info():
    while True:
        if not check_res():
            print("Not enough resources. Please fill them.")
        print("""\nWhat would you like to do?
        1.Get info about total amount of money you earn.
        2.Get more detailed info about money you earn(year/month/day).
        3.Refill resources""")
        per_day()
        try:
            choice = int(input("Enter your choice (1 or 2): ").strip())
            match choice:
                case 1:
                    with open("per_day.json", "r") as f:
                        data = json.load(f)
                        print(f"Total earnings: ${data["total"]}")
                    time.sleep(2)
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                case 2:
                    with open("per_day.json", "r") as f:
                        data = json.load(f)
                    years = [year for year in data if year != "total"]
                    print("Choose a year:")
                    for i, year in enumerate(years, 1):
                        print(f"{i}. {year}")
                    print("If you want to start again, enter '9999'")
                    year_selected=check_choice(years)
                    if not year_selected:
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
                    month_selected = check_choice(months)
                    if not month_selected:
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
                    day_selected = check_choice(days)
                    if not day_selected:
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
                case 3:
                    logging.basicConfig(filename='coffee_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
                    logging.info("water_ml=1000, milk_ml=1000, coffee_g=100, cacao_g=100")
                    logging.info("Resources refilled")
                    print("Refilling resources...")
                    time.sleep(1)
                    print("Resources refilled\nGoing back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                case _:
                    print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Please enter a number.")

def per_day():
    money_per_day = {}
    money_per_month = {}
    money_per_year = {}
    total_per_all_days = 0.0
    total_per_all_months = 0.0
    total_per_all_years = 0.0
    with open("money.log", "r", encoding="utf-8") as file_logs:
        lines = file_logs.read().split("\n")
        for n in lines[:-1]:
            line = n.split(" ")
            year, month, day = line[0].split("-")
            money_per_day[line[0]] = money_per_day.get(line[0], 0) + float(line[-1].strip("$"))
            year_month = f"{year}-{month}"
            money_per_month[year_month] = money_per_day
            money_per_year[year] = money_per_month
        for n in money_per_day:
            total_per_all_days += money_per_day[n]
        money_per_day["total_for_month"] = money_per_month.get("total_for_month", 0.0) + total_per_all_days
        for _ in money_per_month:
            total_per_all_months += money_per_day["total_for_month"]
        money_per_month["total_for_year"] = money_per_month.get("total_for_year", 0.0) + total_per_all_months
        for _ in money_per_year:
            total_per_all_years += money_per_month["total_for_year"]
        money_per_year["total"] = money_per_year.get("total", 0.0) + total_per_all_years
        with open("per_day.json", "w", encoding="utf-8") as per_day_file:
            json.dump(money_per_year, per_day_file, indent=5)

if __name__ == "__main__":
    print("Welcome to COFFEE MACHINE INFO")
    get_info()