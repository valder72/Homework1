def number():
    try:
        n = int(input("Введіть число від -5 до 10: "))
        if -5 <= n <= 10:
            for i in range(1, 11):
                print(f"{n} * {i} = {n * i}")
        else:
            print("Error")
    except ValueError:
        print("Error")
number()