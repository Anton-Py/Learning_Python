def get_temperature_in_fahrenheit(temperature_in_celsius):
    return 9 / 5 * temperature_in_celsius + 32


def get_temperature_in_kelvin(temperature_in_celsius):
    return temperature_in_celsius + 273.15


entered_temperature_in_celsius = float(input("Введите температуру в градусах цельсия: "))

temperature_in_fahrenheit = get_temperature_in_fahrenheit(entered_temperature_in_celsius)
temperature_in_kelvin = get_temperature_in_kelvin(entered_temperature_in_celsius)

print(f"Температура в градусах Фаренгейта равна: {temperature_in_fahrenheit}\n"
      f"температура в градусах Кельвина равна: {temperature_in_kelvin}")
