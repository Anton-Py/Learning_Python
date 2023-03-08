deposit_amount = float(input("Введите сумму вклада: "))
contract_period = int(input("Введите срок договора в месяцах: "))
annual_rate = float(input("Введите размер годовой ставки: "))

ONE_HUNDRED_PERCENT = 100
MONTHS_QUANTITY_IN_YEAR = 12

deposit_on_amount_period_end = deposit_amount * pow(
    1 + annual_rate / ONE_HUNDRED_PERCENT / MONTHS_QUANTITY_IN_YEAR, contract_period)
print(f"Ваш итоговый доход: {deposit_on_amount_period_end:.2f}")

profit = deposit_on_amount_period_end - deposit_amount
print(f"Ваша прибыль: {profit:.2f}")
