class Range:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def number_from(self):
        return self.__start

    @number_from.setter
    def number_from(self, start):
        self.__start = start

    @property
    def number_to(self):
        return self.__end

    @number_to.setter
    def number_to(self, end):
        self.__end = end

    def get_calculate_length(self):
        return self.__end - self.__start

    def is_inside(self, number_check):
        return self.__start <= number_check <= self.__end

    def print(self):
        print(self.__start, self.__end)


number_start = float(input("Введите начальное число диапазона: "))
number_end = float(input("Введите конечное число диапазона: "))
number_to_check = float(input("Введите число, для проверки принадлежности диапазону: "))

numbers_range = Range(number_start, number_end)
print(numbers_range.get_calculate_length())
print(numbers_range.is_inside(number_to_check))
