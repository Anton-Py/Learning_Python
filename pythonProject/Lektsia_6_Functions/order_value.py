SMALL_DISCOUNT = 0.05
BIG_DISCOUNT = 0.10
PRODUCTS_PRICE_FOR_DISCOUNT = 1000
PRODUCTS_QUANTITY_FOR_DISCOUNT = 10


def get_calculation_order_cost(product_quantity_1, product_quantity_2, product_price_1, product_price_2):
    products_quantity = product_quantity_1 + product_quantity_2
    cash_sum = product_price_1 + product_price_2

    if products_quantity >= PRODUCTS_QUANTITY_FOR_DISCOUNT and cash_sum >= PRODUCTS_PRICE_FOR_DISCOUNT:
        products_price_including_discount = cash_sum - cash_sum * BIG_DISCOUNT
    elif products_quantity >= PRODUCTS_QUANTITY_FOR_DISCOUNT:
        products_price_including_discount = cash_sum - cash_sum * SMALL_DISCOUNT
    elif cash_sum >= PRODUCTS_PRICE_FOR_DISCOUNT:
        products_price_including_discount = cash_sum - cash_sum * SMALL_DISCOUNT
    else:
        products_price_including_discount = cash_sum

    return products_price_including_discount


print("Стоимость заказа равна:", get_calculation_order_cost(3, 5, 500, 800))
print("Стоимость заказа равна:", get_calculation_order_cost(4, 7, 600, 500))
print("Стоимость заказа равна:", get_calculation_order_cost(4, 6, 300, 200))
print("Стоимость заказа равна:", get_calculation_order_cost(4, 2, 300, 300))
