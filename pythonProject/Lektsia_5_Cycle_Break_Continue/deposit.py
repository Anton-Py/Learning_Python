deposit_amount = int(input("Введите сумму вклада: "))
contract_period = int(input("Введите срок договора в месяцах: "))
annual_rate = float(input("Введите размер годовой ставки: "))

total_profit = deposit_amount * pow((1 + annual_rate / 100 / 12), contract_period)
print(f"Ваш итоговый доход: {total_profit:.2f}")

margin = total_profit - deposit_amount
print(f"Ваша прибыль: {margin:.2f}")
