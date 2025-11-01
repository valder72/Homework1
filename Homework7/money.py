def money_amount():
    total = 0.0
    with open("money.log", "r", encoding="utf-8") as file_logs:
        lines = file_logs.read().split("\n")
        for n in lines[:-1]:
            line = n.split(" ")
            total += float(line[-1].strip("$"))
    with open("tot_m.txt", "w", encoding="utf-8") as money:
        money.write(f"total: ${total:.2f}\n")
"""def per_day():
    """
if __name__ == "__main__":
    money_amount()