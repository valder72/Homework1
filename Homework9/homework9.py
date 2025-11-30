from utils import calculate_average
def main():
    user_input = input("Введіть числа через пробіл: ")
    try:
        number_list = [float(x) for x in user_input.split()]
        average = calculate_average(number_list)
        print(f"Середнє значення: {average}")
    except ValueError:
        print("Помилка: Будь ласка, вводьте тільки цифри, розділені пробілами.")
if __name__ == "__main__":
    main()