class Order:
    """
        класс Заказ
        Атрибуты:
        products - список  заказов

        Методы:
        __init__
        __str__
        add_order добавить заказ клиенту
        """
    _total_orders = 0
    _total_sum = 0
    __type = "Order"

    def __init__(self, products):
        self.products = products
        Order._total_orders += 1
        Order._total_sum += self.total_price()

    def total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        product_str = f"Заказ (Общая цена = {self.total_price()})"
        for product in self.products:
            product_str = f"{product_str}{product}\n"
        return product_str

    def add_product(self, product):
        self.products.append(product)

    @classmethod
    def total_orders(cls):
        return cls._total_orders

    @classmethod
    def total_sum(cls):
        return cls._total_sum


