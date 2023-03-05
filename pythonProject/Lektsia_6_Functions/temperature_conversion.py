temperature_celsius = float(input("Введите температуру в градусах цельсия: "))


def get_conversion_temperature_to_fahrenheit(temperature):
    return 9 / 5 * temperature + 32


def get_conversion_temperature_to_kelvin(temperature):
    return temperature + 273.15


temperature_in_fahrenheit = get_conversion_temperature_to_fahrenheit(temperature_celsius)
temperature_in_kelvin = get_conversion_temperature_to_kelvin(temperature_celsius)

print(f"Температура в градусах Фаренгейта равна: {temperature_in_fahrenheit}\n"
      f"температура в градусах Кельвина равна: {temperature_in_kelvin}")
