floor_number = 6
entrance_number = 5
apartments_total_number = 81
apartments_number_on_floor = 4

print("all: ", floor_number * entrance_number * apartments_number_on_floor)
if (floor_number * entrance_number * apartments_number_on_floor) < apartments_total_number:
    print("Квартиры с таким номером нет в доме")

else:
    if apartments_total_number % 4 > 0:
        floor_all = apartments_total_number // 4 + 1
        print("floor_all_1", floor_all)
    else:
        floor_all = apartments_total_number // 4
        print("floor_all_2", floor_all)

    if floor_all % floor_number % 4 > 0:
        entrance = floor_all // floor_number + 1
        print("entrance_1", entrance)
    else:
        entrance = floor_all // floor_number
        print("entrance_2", entrance)

    entrance_floor = floor_all - floor_number * (entrance - 1)
    print("entrance_floor", entrance_floor)

    position = apartments_total_number % apartments_number_on_floor
    print("position", position)
    if position == 1:
        print("Ближняя слева, квартира")
    elif position == 2:
        print("Дальняя слева, квартира")
    elif position == 3:
        print("Дальняя справа, квартира")
    else:
        print("Ближняя справа")
