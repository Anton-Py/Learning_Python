from multipledispatch import dispatch


def get_type_name(data):
    if isinstance(data, str):
        print("Это строка")
    elif isinstance(data, int):
        print("Это целое число")
    elif isinstance(data, complex):
        print("Это комплексное число")
    elif isinstance(data, float):
        print("Это число с плавающей точкой")
    elif isinstance(data, bool):
        print("Это булево значение")


get_type_name(data="qwerty")
get_type_name(data=1)
get_type_name(data=3 + 4j)
get_type_name(data=1.5)
get_type_name(data=False)


@dispatch(int)
def get_type_name(data):
    print("Это целое число")


@dispatch(str)
def get_type_name(data):
    print("Это строка")


@dispatch(float)
def get_type_name(data):
    print("Это число с плавающей точкой")


@dispatch(complex)
def get_type_name(data):
    print("Это комплексное число")


@dispatch(bool)
def get_type_name(data):
    print("Это булево значение")


get_type_name("qwerty")
get_type_name(1)
get_type_name(3 + 4j)
get_type_name(1.5)
get_type_name(False)
