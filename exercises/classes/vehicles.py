class Vehicle:
    def __init__(self, color, occupancy, fuel, mobility):
        self.color = color
        self.occupancy = occupancy
        self.fuel = fuel
        self.mobility = mobility

    def drive(self):
        print("Vroom")

    def turn(self, direction):
        print(f'The vehicle turns {direction}')

    def stop(self):
        print(f'The vehicle stops moving')


class Car(Vehicle):
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.horsepower = horsepower
        super().__init__("maroon", 4, "gas", "tires")

    def drive(self, sound):
        print(f'The {self.color} {self.make} drives past with a {sound}')

    def turn(self, direction):
        print(f'The car makes a {direction}')

    def stop(self):
        print(f'The car stops moving on the side of the road')

class Tank(Vehicle):
    def __init__(self, caliber, era):
        self.main_weapon = caliber
        self.era = era
        super().__init__("camo", 2, "diesel", "treads")

    def turn(self, direction):
        print(f'The tank circles to the {direction}')

    def stop(self):
        print(f'The tank stops moving after crushing the cars')

    def drive(self, sound):
        print(f'The {self.color} Tank drives past with a {sound}')

class Airliner(Vehicle):
    def __init__(self, manufacturer, distance):
        self.manufacturer = manufacturer
        self.distance = distance
        super().__init__("white", 200, "diesel", "wings")

    def drive(self, sound):
        print(f'The {self.color} {self.manufacturer} flies past with a {sound}')

class Submarine(Vehicle):
    def __init__(self, country, weapon):
        self.country = country
        self.weapons = weapon
        super().__init__("black", 150, "nucleur", "propulsion")

    def drive(self, sound):
        print(f'The {self.color} {self.country} submarine moves past with a {sound}')

Mustang = Car("Ford", "Shelby", 350)
Mustang.drive("Rumble")
Mustang.turn("left")
Mustang.stop()

M1Abrams = Tank(50, "WWII")
M1Abrams.drive("Crank")
M1Abrams.turn("right")
M1Abrams.stop()

Airbus = Airliner("Boeing", 10000)
Airbus.drive("Whoosh")

Nimitz = Submarine("USA", "Nukes")
Nimitz.drive("quietness")



