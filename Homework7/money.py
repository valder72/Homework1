import json
import time


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
    while True:
        per_day()
        time.sleep(1)