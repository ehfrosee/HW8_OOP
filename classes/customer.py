from order import Order
from product import Product

class Customer:
    """
        класс Клиент
        Атрибуты:
        name - имя клиента
        orders - список  заказов

        Методы:
        __init__
        __str__
        add_order добавить заказ клиенту
        """
    __type = "Customer"

    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def __str__(self):
        name_str = f"Покупатель {self.name}\n"
        for order in self.orders:
            name_str = f"{name_str}{order}\n"
        return name_str

    def __repr__(self):
        name_str = f"Покупатель {self.name}\n"
        for order in self.orders:
            name_str = f"{name_str}{order.repr()}\n"
        return name_str

    @classmethod
    def get_type(cls):
        return cls.__type

    def add_order(self, order):
        self.orders.append(order)



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
