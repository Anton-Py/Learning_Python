deposit_amount = float(input("Введите сумму вклада: "))
contract_period = int(input("Введите срок договора в месяцах: "))
annual_rate = float(input("Введите размер годовой ставки: "))

NUMBER_FOR_ANNUAL_RATE = 100
MONTH_QUANTITY = 12

amount_the_end_period = deposit_amount * pow(1 + annual_rate / NUMBER_FOR_ANNUAL_RATE / MONTH_QUANTITY, contract_period)
print(f"Ваш итоговый доход: {amount_the_end_period:.2f}")

profit = amount_the_end_period - deposit_amount
print(f"Ваша прибыль: {profit:.2f}")
