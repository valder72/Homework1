def replace():
    inpt = input("Введіть цілі числа через пробіл: ")
    res_comp = [int(x) if int(x) >= 0 else 0 for x in inpt.split()]
    result = []
    for num in inpt.split():
        if int(num) < 0:
            result.append(0)
        else:
            result.append(int(num))

    print(f"Результат (loop): {result}")
    print(f"Результат (list comprehension): {res_comp}")
replace()