import logging
import os
import time

if os.path.exists("coffee_logs.log"):
    os.remove("coffee_logs.log")

logging.basicConfig(filename='coffee_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )
logging.info("water_ml=1000, milk_ml=1000, coffee_g=100, cacao_g=100")

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
def check_resources(res, coffee_choice):
    return all([res["water_ml"] >= menu[coffee_choice]["water_ml"],
                res["milk_ml"] >= menu[coffee_choice]["milk_ml"],
                res["coffee_g"] >= menu[coffee_choice]["coffee_g"],
                res["cacao_g"] >= menu[coffee_choice]["cacao_g"]])
def is_invalid_input(input):
    if input == 1:
        return True
    elif input == 2:
        return True
    elif input == 3:
        return True
    elif input == 4:
        return True
    return False
def check_admin():
    name = input("Please enter your name: ")
    password = input("Please enter your password: ")
    return name == "admin" and password == "123456"
def refill_resources(resource):
    print("Refilling resources...")
    resource["water_ml"] = 1000
    resource["milk_ml"] = 1000
    resource["coffee_g"] = 100
    resource["cacao_g"] = 100
    logging.info(f"water_ml={resource['water_ml']}, milk_ml={resource['milk_ml']}, "
                 f"coffee_g={resource['coffee_g']}, cacao_g={resource['cacao_g']}")
    print("Machine refilled successfully!")
    return resource
def get_user_choice():
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
    sizes = {"1": 1.0, "2": 1.5, "3": 2.0}
    invalid_attempts = 0
    while invalid_attempts < 5:
        print("\nChoose size:\n1. Small\n2. Medium\n3. Large")
        size = input("Enter size number: ")
        if size in sizes:
            return sizes[size]
        else:
            print("Invalid size. Try again.")
            invalid_attempts += 1
    print("Too many invalid attempts. Returning to coffee selection...\n")
    return None
def calculate_price(coffee, size_factor):
    base_prices = {"americano": 2.0, "latte": 3.0, "cappuccino": 3.5, "cacao": 2.5}
    return base_prices[coffee] * size_factor
def process_payment(total_price):
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
def make_coffee(resource, coffee_name):
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
menu = {
    "americano": {"water_ml": 250, "milk_ml": 0, "coffee_g": 18, "cacao_g": 0},
    "latte": {"water_ml": 200, "milk_ml": 150, "coffee_g": 24, "cacao_g": 0},
    "cappuccino": {"water_ml": 250, "milk_ml": 100, "coffee_g": 24, "cacao_g": 0},
    "cacao": {"water_ml": 100, "milk_ml": 200, "coffee_g": 0, "cacao_g": 20}
}
def start():
    with open('coffee_logs.log', 'r') as log_file:
        lines = log_file.read().split("\n")
        lines = lines[-2].split(" ")
        resource = resources(lines)
        while True:
            choice = get_user_choice()
            if not choice:
                continue
            if not check_resources(resource, choice):
                print("Not enough resources for that coffee!")
                if check_admin():
                    resource = refill_resources(resource)
                else:
                    print("Please wait for admin to refill.")
                    continue
            size = get_size()
            if not size:
                continue
            price = calculate_price(choice, size)
            if process_payment(price):
                make_coffee(resource, choice)
            else:
                print("Payment failed. No coffee made.")
                continue
            print("Next customer please!\n")
start()