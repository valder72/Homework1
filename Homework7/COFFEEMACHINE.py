import logging
import time
import json


def resources(log_to_check):
    list_resources = {}
    for res in log_to_check:
        res=res.split(" ")
        for item in res:
            if "water_ml" in item:
                list_resources["water_ml"] = int(item[9:-1])
            if "milk_ml" in item:
                list_resources["milk_ml"] = int(item[8:-1])
            if "coffee_g" in item:
                list_resources["coffee_g"] = int(item[9:-1])
            if "cacao_g" in item:
                list_resources["cacao_g"] = int(item[8:])
    return list_resources
def check_resources(resource, coffee_choice, menu):
    logging.info("Checking resources for coffee choice")
    return all([resource["water_ml"] >= menu[coffee_choice]["water_ml"],
                resource["milk_ml"] >= menu[coffee_choice]["milk_ml"],
                resource["coffee_g"] >= menu[coffee_choice]["coffee_g"],
                resource["cacao_g"] >= menu[coffee_choice]["cacao_g"]])
def is_invalid_input(inputs):
    logging.info("Checking if input is invalid")
    if inputs == 1:
        logging.info("Valid input")
        return True
    elif inputs == 2:
        logging.info("Valid input")
        return True
    elif inputs == 3:
        logging.info("Valid input")
        return True
    elif inputs == 4:
        logging.info("Valid input")
        return True
    logging.error("Invalid input")
    return False
def check_admin():
    logging.info("Checking if user is admin")
    name = input("Please enter your name: ")
    password = input("Please enter your password: ")
    return name == "admin" and password == "123456"
def refill_resources(resource):
    logging.info("Refilling resources")
    print("Refilling resources...")
    resource["water_ml"] = 1000
    resource["milk_ml"] = 1000
    resource["coffee_g"] = 100
    resource["cacao_g"] = 100
    logging.info(f"water_ml={resource['water_ml']}, milk_ml={resource['milk_ml']}, "
                 f"coffee_g={resource['coffee_g']}, cacao_g={resource['cacao_g']}")
    print("Machine refilled successfully!")
    logging.info("Resources refilled")
    return resource
def get_user_choice(menu):
    logging.info("Getting user choice")
    print("\nMenu:")
    for i, coffee in enumerate(menu.keys(), 1):
        print(f"{i}. {coffee.capitalize()}")
    invalid_attempts = 0
    while invalid_attempts < 5:
        try:
            choice = int(input("Choose your coffee (1-4): "))
            if choice not in range(1, 5):
                print("Invalid choice! Please try again.")
                logging.error("Invalid input")
                invalid_attempts += 1
            else:
                logging.info(f"User chose {list(menu.keys())[choice - 1]}")
                return list(menu.keys())[choice - 1]
        except ValueError:
            print("Please enter a number!")
            logging.error("Invalid input")
            invalid_attempts += 1
    print("Too many invalid attempts. Returning to menu...")
    logging.error("User input error. Returning to menu...")
    return None
def get_size():
    logging.info("Getting size")
    with open("menu_price.json", "r") as file_menu:
        sizes = json.loads(file_menu.read())["size_price"]
    invalid_attempts = 0
    while invalid_attempts < 5:
        print("\nChoose size:\n1. Small\n2. Medium\n3. Large")
        try:
            size = int(input("Enter size number: "))
            match size:
                case 1:
                    logging.info("User chose small cup")
                    return sizes["small"]
                case 2:
                    logging.info("User chose small cup")
                    return sizes["medium"]
                case 3:
                    logging.info("User chose small cup")
                    return sizes["large"]
                case _:
                    logging.error("Invalid input")
                    print("Invalid size. Try again.")
                    invalid_attempts += 1
        except ValueError:
            print("Invalid size. Try again.")
            logging.info("Invalid input")
            invalid_attempts += 1
    logging.error("User input error. Returning to menu...")
    print("Too many invalid attempts. Returning to main menu...\n")
    return None
def calculate_price(choice, size):
    logging.info("Calculating price")
    with open("menu_price.json", "r") as file_menu:
        base_prices = json.loads(file_menu.read())["price"][choice]
    logging.info(f"Price was calculated ${base_prices * size}")
    return base_prices * size
def process_payment(total_amount):
    logging.info("Processing payment")
    print(f"Your total price: ${total_amount:.2f}")
    logging.info(f"Total price ${total_amount:.2f}")
    with open('coffee_logs.log', 'r', encoding="utf-8") as log_file:
        lines = log_file.read().split("\n")
    with open("money.log", "a") as file_money:
        file_money.write(f"{lines[-2]}\n")
    attempts = 0
    while attempts < 5:
        try:
            payment = float(input("Insert payment amount: $"))
            if payment >= total_amount:
                change = payment - total_amount
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                print("Payment successful!\n")
                logging.info("Payment successful!")
                return True
            else:
                print("Not enough money. Please insert full amount.")
                logging.error("Not enough money.")
                attempts += 1
        except ValueError:
            attempts += 1
            logging.error("Invalid input.")
            print("Please enter a valid amount.")
    logging.error("Not enough money or invalid input. Returning to menu...")
    print("Too many invalid payment attempts. Payment failed.\n")
    return False
def make_coffee(resource, coffee_name, menu):
    logging.info("Making drink")
    print(f"Making your {coffee_name.capitalize()}...")
    time.sleep(2)
    for key in resource:
        resource[key] -= menu[coffee_name][key]
    logging.info(f"Made {coffee_name}, "
                 f"water_ml={resource['water_ml']}, "
                 f"milk_ml={resource['milk_ml']}, "
                 f"coffee_g={resource['coffee_g']}, "
                 f"cacao_g={resource['cacao_g']}")
    print(f"{coffee_name.capitalize()} is ready!\n")
    logging.info("Made drink successfully!")
def additional(resource, menu):
    logging.info("Asking for an additional product")
    total_price = 0
    attempts = 0
    choice_list = []
    while True:
        choices = input("Would you like another drink? (y/n): ").strip().lower()
        if choices in ("y", "yes"):
            logging.info("User agreed for an additional drink")
            while True:
                choice = get_user_choice(menu)
                choice_list.append(choice)
                if not choice:
                    continue
                if not check_resources(resource, choice, menu):
                    logging.error(f"Not enough resources for {choice}")
                    print("Not enough resources for that drink!")
                    attempts += 1
                    if attempts >= 5:
                        print("Too many failed attempts.")
                        return False
                    continue
                size = get_size()
                if not size:
                    continue
                drink_price = calculate_price(choice, size)
                total_price += drink_price
                logging.info(f"Added {choice} ({size}) for ${drink_price:.2f}")
                break
        elif choices in ("n", "no"):
            logging.info("User declined an additional drink")
            break
        else:
            print("Please answer 'y' or 'n'.")
    return [total_price, choice_list]
def start():
    logging.info("water_ml=1000, milk_ml=1000, coffee_g=100, cacao_g=100")
    with open('coffee_logs.log', 'r', encoding="utf-8") as log_file:
        lines = log_file.read().split("\n")
        lines = lines[-2].split(" ")
        resource = resources(lines)
        while True:
            with open('menu_price.json', 'r', encoding="utf-8") as log_f:
                menu = json.load(log_f)["menu"]
            logging.info("Starting new process")
            print("\nHello! What would you like?")
            choice = get_user_choice(menu)
            if not choice:
                continue
            if not check_resources(resource, choice, menu):
                logging.error("Not enough resources")
                print("Not enough resources for that coffee!")
                if check_admin():
                    logging.info("admin came")
                    resource = refill_resources(resource)
                else:
                    print("Please wait for admin to refill.")
                    logging.info("admin didn't come")
                    continue
            logging.info("Enough resources")
            size = get_size()
            if not size:
                continue
            x = additional(resource, menu)
            choices = [choice]
            if x[0]:
                price = calculate_price(choice, size) + x[0]
                for i in x[1]:
                    choices.append(i)
            else:
                price = calculate_price(choice, size)
            if process_payment(price):
                for n in choices:
                    make_coffee(resource, n, menu)
            else:
                logging.error("Payment failed. No coffee made.")
                print("Payment failed. No coffee made.")
                continue
            print("Thank you for choosing us!")
            print("Next customer please!\n")
            logging.info("Ending process")
if __name__ == "__main__":
    logging.basicConfig(filename='coffee_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    with open('coffee_logs.log', 'w') as log:
        log.write("Welcome to COFFEE MACHINE!\n")
    with open("money.log", "w", encoding="utf-8") as file:
        file = file.write("")
    start()

