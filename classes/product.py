class Product:
    """
    класс Продукт
    Атрибуты:
    name - название товара
    price - цена товара

    Методы:
    __init__
    __str__
    compare - сравнение товара с другим по цене
    """
    __type = "Product"

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"

    def __repr__(self):
        return f"Продукт (Название={self.name!r}, Цена={self.price!r})"

    @classmethod
    def get_type(cls):
        return cls.__type

    def __eq__(self, other): return self.price == other.price
    def __ne__(self, other): return not (self == other)

    def __gt__(self, other): return self.price > other.price
    def __le__(self, other): return not (self > other)

    def __lt__(self, other): return self.price < other.price
    def __ge__(self, other): return not (self < other)

if __name__ == '__main__':
    """
    Тестирование класса
    """
    product1 = Product('Apple', 1.23)
    product2 = Product('Peach', 3.32)
    product3 = Product('Peach', 3.32)

    print(product1)
    print(product2.__repr__() )
    print(product3)
    print(product1 == product2)
    print(product3 == product2)
    print(product1 > product2)
    print(product1.get_type())
