def get_order_cost(product_1_quantity, product_1_cost, product_2_quantity, product_2_cost):
    products_quantity = product_1_quantity + product_2_quantity
    order_cost = product_1_cost * product_1_quantity + product_2_cost + product_2_quantity

    small_discount = 0.05
    big_discount = 0.10
    order_cost_for_discount = 1000
    products_quantity_for_discount = 10

    if products_quantity >= products_quantity_for_discount and order_cost >= order_cost_for_discount:
        orders_cost_including_discount = order_cost - order_cost * big_discount
    elif products_quantity >= products_quantity_for_discount:
        orders_cost_including_discount = order_cost - order_cost * small_discount
    elif order_cost >= order_cost_for_discount:
        orders_cost_including_discount = order_cost - order_cost * small_discount
    else:
        orders_cost_including_discount = order_cost

    return orders_cost_including_discount


print("Стоимость заказа равна:", get_order_cost(3, 270, 5, 250))
print("Стоимость заказа равна:", get_order_cost(5, 260, 7, 250))
print("Стоимость заказа равна:", get_order_cost(4, 230, 6, 220))
print("Стоимость заказа равна:", get_order_cost(1, 215, 2, 220))
