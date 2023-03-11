class Range:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number_check):
        return self.__start <= number_check <= self.__end

    def print(self):
        print(self.__start, self.__end)


start_number = float(input("Введите начальное число диапазона: "))
end_number = float(input("Введите конечное число диапазона: "))
number_to_check = float(input("Введите число, для проверки принадлежности диапазону: "))

numbers_range = Range(start_number, end_number)
print(numbers_range.get_length())
print(numbers_range.is_inside(number_to_check))
