number_of_floors_in_house = int(input("Введите количество этажей: "))
number_of_entrances_in_house = int(input("Введите количество подъездов: "))
apartments_number = int(input("Введите квартиру: "))
number_of_apartments_on_floor = 4

if (number_of_floors_in_house * number_of_entrances_in_house * number_of_apartments_on_floor) < apartments_number:
    print("Квартиры с таким номером нет в доме")
else:
    if apartments_number % 4 > 0:
        floors_without_dividing_into_entrances = apartments_number // 4 + 1
    else:
        floors_without_dividing_into_entrances = apartments_number // 4

    if floors_without_dividing_into_entrances % number_of_floors_in_house % 4 > 0:
        entrance_number = floors_without_dividing_into_entrances // number_of_floors_in_house + 1
    else:
        entrance_number = floors_without_dividing_into_entrances // number_of_floors_in_house

    floor_in_entrance = floors_without_dividing_into_entrances - number_of_floors_in_house * (entrance_number - 1)

    apartment_location = apartments_number % number_of_apartments_on_floor
    if apartment_location == 1:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира ближняя слева")
    elif apartment_location == 2:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира дальняя слева")
    elif apartment_location == 3:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира дальняя справа")
    else:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира ближняя справа")
