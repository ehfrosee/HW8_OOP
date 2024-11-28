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


