from multipledispatch import dispatch


def get_type_name(data):
    if isinstance(data, str):
        return "Это строка"
    elif isinstance(data, int):
        return "Это целое число"
    elif isinstance(data, complex):
        return "Это комплексное число"
    elif isinstance(data, float):
        return "Это число с плавающей точкой"
    elif isinstance(data, bool):
        return "Это булево значение"
    else:
        return "Неучтенный тип"


print(get_type_name("qwerty"))
print(get_type_name(1))
print(get_type_name(3 + 4j))
print(get_type_name(1.5))
print(get_type_name(False))


@dispatch(int)
def get_type_name(data):
    return "Это целое число"


@dispatch(str)
def get_type_name(data):
    return "Это строка"


@dispatch(float)
def get_type_name(data):
    return "Это число с плавающей точкой"


@dispatch(complex)
def get_type_name(data):
    return "Это комплексное число"


@dispatch(bool)
def get_type_name(data):
    return "Это булево значение"


print(get_type_name("qwerty"))
print(get_type_name(1))
print(get_type_name(3 + 4j))
print(get_type_name(1.5))
print(get_type_name(False))
