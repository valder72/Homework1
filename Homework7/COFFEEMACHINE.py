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
    logging.info("checking resources for coffee choice")
    return all([resource["water_ml"] >= menu[coffee_choice]["water_ml"],
                resource["milk_ml"] >= menu[coffee_choice]["milk_ml"],
                resource["coffee_g"] >= menu[coffee_choice]["coffee_g"],
                resource["cacao_g"] >= menu[coffee_choice]["cacao_g"]])
def is_invalid_input(inputs):
    logging.info("checking if input is invalid")
    if inputs == 1:
        return True
    elif inputs == 2:
        return True
    elif inputs == 3:
        return True
    elif inputs == 4:
        return True
    return False
def check_admin():
    logging.info("checking if user is admin")
    name = input("Please enter your name: ")
    password = input("Please enter your password: ")
    return name == "admin" and password == "123456"
def refill_resources(resource):
    logging.info("refilling resources")
    print("Refilling resources...")
    resource["water_ml"] = 1000
    resource["milk_ml"] = 1000
    resource["coffee_g"] = 100
    resource["cacao_g"] = 100
    logging.info(f"water_ml={resource['water_ml']}, milk_ml={resource['milk_ml']}, "
                 f"coffee_g={resource['coffee_g']}, cacao_g={resource['cacao_g']}")
    print("Machine refilled successfully!")
    return resource
def get_user_choice(menu):
    logging.info("getting user choice")
    print("\nMenu:")
    for i, coffee in enumerate(menu.keys(), 1):
        print(f"{i}. {coffee.capitalize()}")
    invalid_attempts = 0
    while invalid_attempts < 5:
        try:
            choice = int(input("Choose your coffee (1-4): "))
            if choice not in range(1, 5):
                print("Invalid choice! Please try again.")
                invalid_attempts += 1
            else:
                return list(menu.keys())[choice - 1]
        except ValueError:
            print("Please enter a number!")
            invalid_attempts += 1
    print("Too many invalid attempts. Returning to menu...")
    return None
def get_size():
    logging.info("getting size")
    with open("menu_price.json", "r") as file:
        sizes = json.loads(file.read())["size_price"]
    invalid_attempts = 0
    while invalid_attempts < 5:
        print("\nChoose size:\n1. Small\n2. Medium\n3. Large")
        try:
            size = int(input("Enter size number: "))
            match size:
                case 1:
                    return sizes["small"]
                case 2:
                    return sizes["medium"]
                case 3:
                    return sizes["large"]
                case _:
                    print("Invalid size. Try again.")
                    invalid_attempts += 1
        except ValueError:
            print("Invalid size. Try again.")
            invalid_attempts += 1
    print("Too many invalid attempts. Returning to coffee selection...\n")
    return None
def calculate_price(choice, size_factor):
    logging.info("calculating price")
    with open("menu_price.json", "r") as file:
        base_prices = json.loads(file.read())["price"][choice]
    return base_prices * size_factor
def process_payment(total_price):
    logging.info("processing payment")
    print(f"Your coffee will cost: ${total_price:.2f}")
    attempts = 0
    while attempts < 5:
        try:
            payment = float(input("Insert payment amount: $"))
            if payment >= total_price:
                change = payment - total_price
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                print("Payment successful!\n")
                return True
            else:
                print("Not enough money. Please insert full amount.")
                attempts += 1
        except ValueError:
            attempts += 1
            print("Please enter a valid amount.")
    print("Too many invalid payment attempts. Payment failed.\n")
    return False
def make_coffee(resource, coffee_name, menu):
    logging.info("making coffee")
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
def additional(resource, menu):
    logging.info("adding additional product")
    while True:
        print("Would you like to add something extra?")
        choice = input("Add something? (y/n): ")
        i = 0
        price = 0
        if choice.lower() in "yes" :
            while True:
                choice = get_user_choice(menu)
                if not choice:
                    continue
                if not check_resources(resource, choice, menu):
                    print("Not enough resources for that coffee!")
                    if i < 5:
                        i += 1
                    elif i == 5:
                        return False
                size = get_size()
                if not size:
                    continue
                price += calculate_price(choice, size)
                return [price,choice]
        else:
            return False
def start():
    logging.info("water_ml=1000, milk_ml=1000, coffee_g=100, cacao_g=100")
    with open('coffee_logs.log', 'r') as log_file:
        lines = log_file.read().split("\n")
        lines = lines[-2].split(" ")
        resource = resources(lines)
        while True:
            with open('menu_price.json', 'r') as log_f:
                menu = json.load(log_f)["menu"]
            logging.info("starting new process")
            print("\nHello! What would you like?")
            choice = get_user_choice(menu)
            if not choice:
                continue
            if not check_resources(resource, choice, menu):
                print("Not enough resources for that coffee!")
                if check_admin():
                    resource = refill_resources(resource)
                else:
                    print("Please wait for admin to refill.")
                    continue
            size = get_size()
            if not size:
                continue
            x=additional(resource, menu)
            choices = [choice]
            if x:
                price = calculate_price(choice, size) + x[0]
                choices.append(x[1])
            else:
                price = calculate_price(choice, size)
            if process_payment(price):
                for n in choices:
                    make_coffee(resource, n, menu)
            else:
                print("Payment failed. No coffee made.")
                continue
            print("Thank you for choosing us!")
            print("Next customer please!\n")
            logging.info("ending process")
if __name__ == "__main__":
    logging.basicConfig(filename='coffee_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    with open('coffee_logs.log', 'w') as log:
        log.write("Welcome to COFFEE MACHINE!\n")
    start()

