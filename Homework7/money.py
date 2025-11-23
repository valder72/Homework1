import json
import time
import logging
from json import JSONDecodeError
import matplotlib.pyplot as plt
def save_to_another_file(data):
    error = 0
    while True:
        if error == 5:
            return False
        try:
            cho = int(input("Would you to save changes in 1.current file(menu_price.json) or 2.another?(print number): "))
            match cho:
                case 1:
                    with open('menu_price.json', 'w', encoding="utf-8") as f:
                        f.write(json.dumps(data, indent=4))
                        return "menu_price.json"

                case 2:
                    name = input("Type name of file(max length 32 and word 'menu' in it): ").lower().replace(" ", "_")
                    name +=".json"
                    if name == "menu_price.json":
                        print("filename already exists.")
                        error += 1
                        continue
                    if len(name) > 32 or "menu" not in name.lower().split("_"):
                        print("Too long or doesn't have 'menu' in it.")
                        error += 1
                        continue
                    with open(name, 'w') as f:
                        f.write(json.dumps(data, indent=4))
                    return name
        except ValueError:
            print("Invalid input")
            error += 1
            if error == 5:
                print("Too many wrong attempts")
                return False
def manage_coffee():
    with open("menu_price.json", "r", encoding="utf-8") as data:
        data = json.load(data)
    error = 0
    while True:
        if error == 5:
            return False
        try:
            action = int(input("What would you like to do?(print number)\n1.Add\n2.Delete\n3.Change\n4.Change size price\nIf you want to go back print '9999'.\nInput:"))
            match action:
                case 9999:
                    print("Goodbye!")
                    return False
                case 1:
                    name = input("Name: ").lower().strip()
                    for j in data['price'].keys():
                        if name in j:
                            print("Coffee already exists.")
                    error = 0
                    while True:
                        if error == 5:
                            return False
                        try:
                            price = float(input("Price: "))
                            w = int(input("Water ml (<300): "))
                            if not (w <= 300):
                                print("Water must be under 300 ml!")
                                error+=1
                                continue
                            m = int(input("Milk ml (<300): "))
                            if m >= 300:
                                print("Milk must be under 300 ml!")
                                error += 1
                                continue
                            cof = int(input("Coffee g (<40): "))
                            if cof >= 40:
                                print("Coffee must be under 40 g!")
                                error += 1
                                continue
                            ca = int(input("Cacao g (<40): "))
                            if ca >= 40:
                                print("Cacao must be under 40 g!")
                                error += 1
                                continue
                            data['price'][name] = price
                            data['menu'][name] = {"water_ml": w, "milk_ml": m, "coffee_g": cof, "cacao_g": ca}
                            print(f"Added {name} with price {price}$ and resources {data['price'][name]}.")
                            return data
                        except ValueError:
                            print("Invalid input.")
                            error += 1
                            if error == 5:
                                return False
                case 2:
                    print("Menu: ")
                    i_list=[]
                    for i, coffee in enumerate(data["price"].keys(), 1):
                        print(f"{i}. {coffee.capitalize()}")
                        i_list.append((i, coffee))
                    error=0
                    try:
                        name = int(input("Which coffee to delete?(number): "))
                        for m in i_list:
                            if name == m[0]:
                                del data['price'][m[1]]
                                del data['menu'][m[1]]
                                print(f"Deleted {m[1]}.")
                            else:
                                print("Coffee not found.")
                        return data
                    except ValueError:
                        print("Invalid input.")
                        error += 1
                        if error == 5:
                            return False
                case 3:
                    print("Menu: ")
                    i_list = []
                    for i, coffee in enumerate(data["price"].keys(), 1):
                        print(f"{i}. {coffee.capitalize()}")
                        i_list.append((i, coffee))
                    error=0
                    try:
                        inp = int(input("Name to change(number): "))
                        name = i_list[inp-1][1]
                        if name in data['price']:
                            sub_action = int(input("What do you want to update?\n1.Price\n2.Resources\nInput: "))
                            error = 0
                            try:
                                match sub_action:
                                    case 1:
                                        error = 0
                                        try:
                                            new_p_size = float(input(f"New price (current {data['price'][name]}): "))
                                            data['price'][name] = new_p_size
                                            return data
                                        except ValueError:
                                            print("Invalid input.")
                                            error += 1
                                            if error == 5:
                                                return False
                                    case 2:
                                        print("Enter new value or press Enter to keep current.")
                                        error = 0
                                        while True:
                                            if error == 5:
                                                return False
                                            try:
                                                w = int(input(f"Water ml (<300)(current {data['menu'][name]["water_ml"]}): "))
                                                if not (w <= 300):
                                                    print("Water must be under 300 ml!")
                                                    error+=1
                                                    continue
                                                m = int(input(f"Milk ml (<300)(current {data['menu'][name]["milk_ml"]}): "))
                                                if m >= 300:
                                                    print("Milk must be under 300 ml!")
                                                    error += 1
                                                    continue
                                                cof = int(input(f"Coffee g (<40)(current {data['menu'][name]["coffee_g"]}): "))
                                                if cof >= 40:
                                                    print("Coffee must be under 40 g!")
                                                    error += 1
                                                    continue
                                                ca = int(input(f"Cacao g (<40)(current {data['menu'][name]["cacao_g"]}): "))
                                                if ca >= 40:
                                                    print("Cacao must be under 40 g!")
                                                    error += 1
                                                    continue
                                                data['menu'][name]["water_ml"] = w
                                                data['menu'][name]["milk_ml"] = m
                                                data['menu'][name]["coffee_g"] = cof
                                                data['menu'][name]["cacao_g"] = ca
                                                return data
                                            except ValueError:
                                                print("Invalid input.")
                                                error += 1
                                                if error == 5:
                                                    return False
                            except ValueError:
                                print("Invalid input.")
                                error += 1
                                if error == 5:
                                    return False
                        else:
                            print("Coffee not found.")
                    except (ValueError, IndexError):
                        print("Invalid input.")
                        error += 1
                        if error == 5:
                            return False
                case 4:
                    error = 0
                    while True:
                        if error == 5:
                            return False
                        try:
                            s_name = int(input("Which size (1.small, 2.medium, 3.large)(enter number)?: "))
                            if s_name in range(1, 4):
                                error = 0
                                try:
                                    new_p_size = float(input(f"New price for {s_name} (current {data['size_price'][s_name]}): "))
                                    data['size_price'][s_name] = new_p_size
                                    print("Size updated.")
                                    return data
                                except ValueError:
                                    print("Invalid number.")
                                    error += 1
                                    if error == 5:
                                        return False
                            else:
                                print("Size not found.Please try again.")
                                error += 1
                                continue
                        except ValueError:
                            print("Invalid input.")
                            error += 1
                            if error == 5:
                                return False
                case _:
                    print("Unknown command.")
        except ValueError:
            print("Invalid input.")
            error += 1
            if error == 5:
                return False
def graphic():
    dict_plot_y = {}
    dict_plot_m = {}
    dict_plot_d = {}
    dict_plot_h = {}
    check_file("per_day.json")
    with open("per_day.json", "r", encoding="utf-8") as f:
        graph = json.load(f)
    for year in graph:
        if year != "total":
            amount_for_year = graph[year]["total_for_year"]
            dict_plot_y[year] = amount_for_year
            for month in graph[year]:
                if month != "total_for_year":
                    amount_for_month = graph[year][month]["total_for_month"]
                    dict_plot_m[month] = amount_for_month
                    for day in graph[year][month]:
                        if day != "total_for_month":
                            amount_for_day = graph[year][month][day]["total_for_day"]
                            dict_plot_d[day] = amount_for_day
                            for hour in graph[year][month][day]:
                                if hour != "total_for_day":
                                    amount_for_hour = graph[year][month][day][hour]
                                    dict_plot_h[f"{day} - {hour}"] = amount_for_hour
    e=0
    while True:
        try:
            choice = int(input("""Would you like to see by:
1.year
2.month
3.day
4.time
If you want to go back print '9999'.
Choice: """).strip())
            if choice == 9999:
                return False
            if not 1 <= choice <= 4:
                print("Invalid choice.")
                e += 1
                if e == 5:
                    return False
            break
        except (ValueError, IndexError):
            print("Invalid choice.")
            e+=1
            if e == 5:
                return False
    match choice:
        case 1:
            plt.bar(list(dict_plot_y.keys()), list(dict_plot_y.values()))
            plt.title("Money per year")
            plt.ylabel("Money")
            plt.xlabel("Year")
            plt.show()
        case 2:
            plt.bar(list(dict_plot_m.keys()), list(dict_plot_m.values()))
            plt.title("Money per month")
            plt.ylabel("Money")
            plt.xlabel("Month")
            plt.show()
        case 3:
            plt.bar(list(dict_plot_d.keys()), list(dict_plot_d.values()))
            plt.title("Money per day")
            plt.ylabel("Money")
            plt.xlabel("Day")
            plt.show()
        case 4:
            plt.bar(list(dict_plot_h.keys()), list(dict_plot_h.values()))
            plt.title("Money per time")
            plt.ylabel("Money")
            plt.xlabel("Time")
            plt.xticks(rotation='vertical')
            plt.tight_layout()
            plt.show()

def check_file(file_name):
    try:
        with open(file_name,"r", encoding="utf-8") as f:
            f.read()
        return True
    except (FileNotFoundError, UnicodeDecodeError, IOError, JSONDecodeError) as e:
        logging.error(f"Could not access file '{file_name}': {e}")
        return False
def check_res():
    if not check_file("coffee_logs.log"):
        print("File corrupted.")
        return "error"
    with open("coffee_logs.log", "r", encoding="utf-8") as res_file:
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
        if check_res() == "error":
            continue
        print("""\nWhat would you like to do?
1.Get info about total amount of money you earn.
2.Get more detailed info about money you earn(year/month/day).
3.Refill resources
4.View sales amount by year/month/day/time
5.Work with menu""")
        if not per_day():
            continue
        else:
            per_day()
        try:
            choice = int(input("Enter your choice (1 or 5): ").strip())
            match choice:
                case 1:
                    if not check_file("per_day.json"):
                        print("File corrupted.")
                        continue
                    with open("per_day.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        print(f"Total earnings: ${data["total"]}")
                    time.sleep(2)
                    print("Going back to main menu...")
                    time.sleep(1)
                    print("Welcome back")
                    continue
                case 2:
                    if not check_file("per_day.json"):
                        print("File corrupted.")
                        continue
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
                    amount = data[year_selected][month_selected][day_selected]["total_for_day"]
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
                case 4:
                    fls=graphic()
                    if not fls:
                        time.sleep(2)
                        print("Going back to main menu...")
                        time.sleep(1)
                        print("Welcome back")
                case 5:
                    if not check_file("menu_price.json"):
                        time.sleep(1)
                        print("Going back to main menu...")
                        time.sleep(1)
                        print("Welcome back")
                        continue
                    p = manage_coffee()
                    if not p:
                        time.sleep(1)
                        print("Going back to main menu...")
                        time.sleep(1)
                        print("Welcome back")
                        continue
                    v = save_to_another_file(p)
                    if not v:
                        time.sleep(1)
                        print("Going back to main menu...")
                        time.sleep(1)
                        print("Welcome back")
                        continue
                    elif v == "menu_price.json":
                        print("File 'menu_price.json' was changed")
                        time.sleep(1)
                        print("Going back to main menu...")
                        time.sleep(1)
                        print("Welcome back")
                        continue
                    else:
                        print(f"File {v} was changed")
                        time.sleep(1)
                        print("Going back to main menu...")
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
    money_per_time={}
    total_for_day=0.0
    total_per_all_days = 0.0
    total_per_all_months = 0.0
    total_per_all_years = 0.0
    d = ""
    if not check_file("money.log"):
        print("File corrupted.")
        return False
    with open("money.log", "r", encoding="utf-8") as file_logs:
        lines = file_logs.read().split("\n")
        for n in lines[:-1]:
            line = n.split(" ")
            year, month, day = line[0].split("-")
            hours_minutes_seconds = line[1].split(",")[0]
            year_month_day = f"{year}-{month}-{day}"
            if d != year_month_day:
                d = f"{year_month_day}"
                money_per_time = {}
            money_per_time[hours_minutes_seconds] = money_per_time.get(hours_minutes_seconds, 0) + float(line[-1].strip("$"))
            money_per_day[year_month_day] = money_per_time
            year_month = f"{year}-{month}"
            money_per_month[year_month] = money_per_day
            money_per_year[year] = money_per_month

        for date, t in money_per_day.items():
            for m in t.values():
                total_for_day += m
            money_per_day[date]["total_for_day"] = total_for_day
            total_per_all_days += money_per_day[date]["total_for_day"]
            total_for_day = 0.0
        money_per_day["total_for_month"] = money_per_month.get("total_for_month", 0.0) + total_per_all_days
        for _ in money_per_month:
            total_per_all_months += money_per_day["total_for_month"]
        money_per_month["total_for_year"] = money_per_month.get("total_for_year", 0.0) + total_per_all_months
        for _ in money_per_year:
            total_per_all_years += money_per_month["total_for_year"]
        money_per_year["total"] = money_per_year.get("total", 0.0) + total_per_all_years
        if not check_file("per_day.json"):
            print("File corrupted.")
            return False
        with open("per_day.json", "w", encoding="utf-8") as per_day_file:
            json.dump(money_per_year, per_day_file, indent=5)
        return True
if __name__ == "__main__":
    print("Welcome to COFFE MACHINE!")
    get_info()