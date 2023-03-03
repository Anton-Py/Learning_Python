start_number_range = float(input("Введите начальное число диапазлона: "))
end_number_range = float(input("Введите конечное число диапазона: "))
number_to_check = float(input("Введите число, для проверки принадлежгости диапазону: "))


class Range:
    def __init__(self, number_from, number_to, number_check):
        self.__number_from = number_from
        self.__number_to = number_to
        self.__number_check = number_check

    @property
    def number_from(self):
        return self.__number_from

    @property
    def number_to(self):
        return self.__number_to

    @number_from.setter
    def number_from(self, number_from):
        self.__number_from = number_from

    @number_to.setter
    def number_to(self, number_to):
        self.__number_to = number_to

    def calculate_range_length(self):
        print(self.__number_to - self.__number_from)

    def is_inside(self, ):
        if self.__number_from <= self.__number_check <= self.__number_to:
            return True
        else:
            return False

    def print(self):
        print(self.__number_from, self.__number_to)


range_numbers = Range(start_number_range, end_number_range, number_to_check)

range_numbers.calculate_range_length()
print(range_numbers.is_inside())
