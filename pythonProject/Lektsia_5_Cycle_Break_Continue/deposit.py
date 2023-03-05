deposit_amount = float(input("Введите сумму вклада: "))
contract_period = int(input("Введите срок договора в месяцах: "))
annual_rate = float(input("Введите размер годовой ставки: "))

NUMBER_CALCULATION_ANNUAL_RATE = 100
MONTHS_QUANTITY_YEAR = 12

deposit_amount_end_period = deposit_amount * pow(
    1 + annual_rate / NUMBER_CALCULATION_ANNUAL_RATE / MONTHS_QUANTITY_YEAR, contract_period)
print(f"Ваш итоговый доход: {deposit_amount_end_period:.2f}")

profit = deposit_amount_end_period - deposit_amount
print(f"Ваша прибыль: {profit:.2f}")
