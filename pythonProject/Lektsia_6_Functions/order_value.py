def get_calculation_order_cost(product_quantity_1, product_quantity_2, product_price_1, product_price_2):
    products_quantity = product_quantity_1 + product_quantity_2
    cash_sum = product_price_1 + product_price_2

    small_discount = 0.05
    big_discount = 0.10
    products_price_for_discount = 1000
    products_quantity_for_discount = 10

    if products_quantity >= products_quantity_for_discount and cash_sum >= products_price_for_discount:
        products_price_including_discount = cash_sum - cash_sum * big_discount
    elif products_quantity >= products_quantity_for_discount:
        products_price_including_discount = cash_sum - cash_sum * small_discount
    elif cash_sum >= products_price_for_discount:
        products_price_including_discount = cash_sum - cash_sum * small_discount
    else:
        products_price_including_discount = cash_sum

    return products_price_including_discount


print("Стоимость заказа равна:", get_calculation_order_cost(3, 5, 500, 800))
print("Стоимость заказа равна:", get_calculation_order_cost(4, 7, 600, 500))
print("Стоимость заказа равна:", get_calculation_order_cost(4, 6, 300, 200))
print("Стоимость заказа равна:", get_calculation_order_cost(4, 2, 300, 300))
