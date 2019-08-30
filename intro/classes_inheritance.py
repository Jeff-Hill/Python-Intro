import datetime
# Base Class (or parent class) We won't make instances of
# this directly. IT exists to help us reduce repitition

# Inheritance

class Animal:

    def __init__(self, leg_num, species, owner="Happy Acres Breeding Farm"):
        self.owner = owner
        self.species = species
        self.leg_num = leg_num

    def set_solid_food_date(self):
        self.solid_food_date = datetime.datetime.now().strftime( "%x" )

    def move(self, speed):
        return f"{self.species} moves at {speed} meters per second"




# Derived Class that will inherit behaviors and attributes from Animal

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__( 4, "dog")

collie = Dog("collie")
print(collie)

class RaceHorse(Animal):
    def __init__(self):
        self.races_won = []
        super().__init__(4, "horse")

    def add_won_race(self, race):
        self.races_won.append(race)

    def trot(self):
        return self.move(8)

    def gallop(self):
        return self.move(15)

buttercup = RaceHorse()
buttercup.add_won_race("Preakness")
print(buttercup.races_won)

print(collie.leg_num)
print(buttercup.leg_num)
collie.set_solid_food_date()
buttercup.set_solid_food_date()
print(buttercup.trot())
print(buttercup.gallop())