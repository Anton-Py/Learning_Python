floors_quantity = int(input("Введите количество этажей: "))
entrances_quantity = int(input("Введите количество подъездов: "))
apartment_amount = int(input("Введите квартиру: "))

apartments_quantity_on_floor = 4

if (floors_quantity * entrances_quantity * apartments_quantity_on_floor) < apartment_amount:
    print("Квартиры с таким номером нет в доме")
else:
    entrance_number = (apartment_amount - 1) // (floors_quantity * apartments_quantity_on_floor) + 1
    print(f"Номер подъезда: {entrance_number}")

    floor_number = \
        (apartment_amount - 1) % floors_quantity * apartments_quantity_on_floor // apartments_quantity_on_floor + 1
    print(f"Номер этажа: {floor_number}")

    apartment_location = apartment_amount % apartments_quantity_on_floor

    if apartment_location == 1:
        print(f"Квартира ближняя слева")
    elif apartment_location == 2:
        print(f"Квартира дальняя слева")
    elif apartment_location == 3:
        print(f"Квартира дальняя справа")
    else:
        print(f"Квартира ближняя справа")
