class Discount:
    """
    Класс скидок
    Атрибуты:
    discount_name - название скидки
    discount_size - размер скидки

    Методы:
    __init__
    __str__
    add_order добавить заказ клиенту

    """

    __type = "Discount"
    _discounts = {}

    def __init__(self, discount_name, discount_size):
        self.discount_name = discount_name
        self.discount_size = discount_size
        Discount._discounts[discount_name] = discount_size

    @staticmethod
    def get_discount(order, discount_name):
        price = order.total_price()
        discount = price * Discount._discounts[discount_name] * 0.01
        final_price = price - discount
        return f"Скидка \"{discount_name}\". Размер скидки {discount}\nОкончательная стоимость заказа {final_price}"

    @classmethod
    def discounts(cls):
        return cls._discounts

    def __str__(self):
        return f"Скидка (Название=\"{self.discount_name}\", размер={self.discount_size}%)"


if __name__ == "__main__":

    dsc1 = Discount("Промокод", 3)
    dsc2 = Discount("Выходной день", 5)
    print(dsc1)
    print(dsc2)
    print(Discount.discounts())

