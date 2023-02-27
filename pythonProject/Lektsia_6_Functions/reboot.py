def get_type_name(data):
    if isinstance(data, str):
        print("Это строка")


def get_type_name(data):
    if isinstance(data, int):
        print("Это целое число")


def get_type_name(data):
    if isinstance(data, complex):
        print("Это комплексное число")


def get_type_name(data):
    if isinstance(data, float):
        print("Это число с плавающей точкой")


def get_type_name(data):
    if isinstance(data, bool):
        print("Это булево значение")


get_type_name(data="qwerty")
get_type_name(data=1)
