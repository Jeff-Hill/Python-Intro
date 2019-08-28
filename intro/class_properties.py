class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'The {self.name} costs ${self.price}'


car = Product("Mustang", 100)
car.price = "fish"
print(car)

# To protect the properties on the object
class Product:
    def __init__(self, name):
        self.name = name
    # Define a getter
    @property
    def price(self):
        try:
            return self.__price

        except AttributeError:
            return 0
    # Define the setter
    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self.__price = price
        else:
            print("Gotta use a float, dummy")

    def __str__(self):
        return f'The {self.name} costs ${self.price}'


car = Product("Mustang")
print(car.name)
car.price = 5000.00
print(car)
