from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount

if __name__ == '__main__':
    """
    Тестирование класса
    """
    product1 = Product('Apple', 1.23)
    product2 = Product('Peach', 3.32)
    product3 = Product('Orange', 2.47)

    print(f"Продукт\n{product1}")

    order1 = Order([product1, product2])
    print(f"Заказ 1:\n{order1}")
    order2 = Order([product3, product1, product3])
    print(f"Заказ 2:\n{order2}")
    order2.add_product(product2)
    print(f"Заказ 2 дополненный:\n{order2}")

    customer1 = Customer("Иван")
    print(customer1)
    customer2 = Customer("Марья")
    print(customer2)

    customer1.add_order(order1)
    customer2.add_order(order2)
    print(f"Покупатель 1\n{customer1}")
    print(f"Покупатель 2\n{customer2}")

    print(f"Общее количество заказов {Order.total_orders()}")
    print(f"Стоимость всех заказов {Order.total_sum()}")

    dsc1 = Discount("Промокод", 3)
    dsc2 = Discount("Выходной день", 5)
    print(Discount.discounts())

    print(order1.total_price())
    print(dsc1)
    print(dsc1.get_discount(order1, "Промокод"))

    print(order2.total_price())
    print(dsc2)
    print(Discount.get_discount(order2, "Выходной день"))


