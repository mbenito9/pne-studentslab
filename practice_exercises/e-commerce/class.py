class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return self.name, self.price
    def get_information(self):
        return f"Product: {self.name} | Price: {self.price}"
class Client(Product):
    def __init__(self, name, shopping_cart, price, email):
        super().__init__(name,price)
        self.shopping_chart = shopping_cart
        self.email = email


s = Product("tom", "1900")
print(s.get_information())

