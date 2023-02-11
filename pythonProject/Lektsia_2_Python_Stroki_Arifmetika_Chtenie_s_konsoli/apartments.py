floors_quantity_in_house = int(input("Введите количество этажей: "))
entrances_quantity_in_house = int(input("Введите количество подъездов: "))
apartment_quantity = int(input("Введите квартиру: "))
apartments_quantity_on_floor = 4

if (floors_quantity_in_house * entrances_quantity_in_house * apartments_quantity_on_floor) < apartment_quantity:
    print("Квартиры с таким номером нет в доме")
else:
    entrance_number = (apartment_quantity - 1) // (floors_quantity_in_house * 4) + 1
    print(f"Номер подъезда: {entrance_number}")
    floor_in_entrance = (apartment_quantity - 1) % (floors_quantity_in_house * 4) // 4 + 1
    print(f"Номер этажа: {floor_in_entrance}")

    apartment_location = apartment_quantity % apartments_quantity_on_floor

    if apartment_location == 1:
        print(f"Квартира ближняя слева")
    elif apartment_location == 2:
        print(f"Квартира дальняя слева")
    elif apartment_location == 3:
        print(f"Квартира дальняя справа")
    else:
        print(f"Квартира ближняя справа")
