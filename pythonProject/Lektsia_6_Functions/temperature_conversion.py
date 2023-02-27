celsius_temperature = int(input("Введите температуру в градусах цельсия: "))


def conversion_temperature_to_fahrenheit(temperature_in_celsius):
    return 9 / 5 * temperature_in_celsius + 32


def conversion_temperature_to_kelvin(temperature_in_celsius):
    return temperature_in_celsius + 273.15


temperature_in_fahrenheit = conversion_temperature_to_fahrenheit(celsius_temperature)
temperature_in_kalvin = conversion_temperature_to_kelvin(celsius_temperature)

print(f"Температура в градусах Фаренгейта равна: {temperature_in_fahrenheit}\n"
      f"температура в градусах Кельвина равна: {temperature_in_kalvin}")
