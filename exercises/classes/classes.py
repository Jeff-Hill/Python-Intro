# Create a Pizza type for representing pizzas in Python. Think about some basic properties
# that would define a pizza's values; things like size, crust type, and toppings would help.
# Define those in the __init__ method so each instance can have its own specific values for those properties.
class Pizza:
    def __init__(self, size, crust, sauce, cheese, topping):
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.topping = topping

# Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, topping):
        self.topping.append (topping)

# Add a method for outputting a description of the pizza (sample output below).

    # def pizza_topping(self, topping):

    def print_order(self):
        topping_str = ' & '.join(self.topping)
        print(f'I would like a {self.size}-inch, {self.crust} pizza with {topping_str} ')


# Make two different instances of a pizza. If you have properly defined
# the class, you should be able to do something like the following
# with your Pizza type.

meat_lovers = Pizza(16, "Thin Crust", "Marinara", "Mozzarella", ["pepperoni", "olives"])
# meat_lovers = Pizza()
# meat_lovers.size = 16
# meat_lovers.crust = "Thin crust"
# meat_lovers.sauce = "Marinara"
# meat_lovers.cheese = "Mozzarella"
# meat_lovers.add_topping("Pepperoni")
# meat_lovers.add_topping("Olives")
print(meat_lovers.print_order())

premium_pizza = Pizza(24, "Stuffed Crust", "Alfredo", "Four Cheese",["onions", "olives", "peppers"])
print(premium_pizza.print_order())

# for prop, value in meat_lovers.__dict__.items():
#     print(f'{prop}:\n{value}\n')

# You should produce output in the terminal similiar
# to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."

