def calculation_order_value(product_1, product_2, cash_sum):
    product_quantity = product_1 + product_2

    if product_quantity >= 10 and cash_sum >= 1000:
        discount_amount = cash_sum - cash_sum * 0.10
    elif product_quantity >= 10:
        discount_amount = cash_sum - cash_sum * 0.05
    elif cash_sum >= 1000:
        discount_amount = cash_sum - cash_sum * 0.05
    else:
        discount_amount = cash_sum

    return discount_amount


print("Стоимость заказа равна:", calculation_order_value(3, 5, 1100))
print("Стоимость заказа равна:", calculation_order_value(4, 7, 1000))
print("Стоимость заказа равна:", calculation_order_value(4, 6, 900))
print("Стоимость заказа равна:", calculation_order_value(4, 2, 900))
