# floors_quantity_in_house = int(input("Введите количество этажей: "))
# entrances_quantity_in_house = int(input("Введите количество подъездов: "))
# apartment_quantity = int(input("Введите квартиру: "))
# apartments_quantity_on_floor = 4

floors_quantity_in_house = 6
entrances_quantity_in_house = 5
apartment_quantity = 81
apartments_quantity_on_floor = 4

if (floors_quantity_in_house * entrances_quantity_in_house * apartments_quantity_on_floor) < apartment_quantity:
    print("Квартиры с таким номером нет в доме")
else:
    if apartment_quantity % 4 > 0:
        floors_without_dividing_into_entrances = apartment_quantity // apartments_quantity_on_floor + 1
    else:
        floors_without_dividing_into_entrances = apartment_quantity // apartments_quantity_on_floor

    if floors_without_dividing_into_entrances % floors_quantity_in_house % apartments_quantity_on_floor > 0:
        entrance_number = floors_without_dividing_into_entrances // floors_quantity_in_house + 1
    else:
        entrance_number = floors_without_dividing_into_entrances // floors_quantity_in_house

    floor_in_entrance = floors_without_dividing_into_entrances - floors_quantity_in_house * (entrance_number - 1)

    apartment_location = apartment_quantity % apartments_quantity_on_floor
    if apartment_location == 1:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира ближняя слева")
    elif apartment_location == 2:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира дальняя слева")
    elif apartment_location == 3:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира дальняя справа")
    else:
        print(f"Номер подъезда: {entrance_number}, номер этажа: {floor_in_entrance}, квартира ближняя справа")

    entrance_number = (apartment_quantity - 1) // (floors_quantity_in_house * 4) + 1
    floor_in_entrance = (apartment_quantity - 1) % (floors_quantity_in_house * 4) // 4 + 1
    print(entrance_number, floor_in_entrance)