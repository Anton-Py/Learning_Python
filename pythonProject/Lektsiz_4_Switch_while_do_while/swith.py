number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
command_code = int(input("Введите код команды: "))

match command_code:
    case 1:
        print(number_1 + number_2)
    case 2:
        print(number_1 - number_2)
    case 3:
        print(number_1 * number_2)
    case 4:
        print(number_1 / number_2)
    case other:
        print("Неизвестная операция")
