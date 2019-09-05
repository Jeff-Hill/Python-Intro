from vehicle import Vehicle
from gasPowered import GasPowered
#  Part 1 - Create a Ford Mustang class
    # * `manufacturer` attribute
    # * `model` attribute
    # * `fuel_capacity` attribute
    # * `gas_level` attribute
    # * `horsepower` attribute
    # * `wheel_count` attribute
    # * `drive()` method lowers `gas_level` by 4 each time it is invoked
    # * `refuel()` method method sets `gas_level` to `fuel_capacity` value

class Mustang(Vehicle, GasPowered):
    def __init__(self):
        Vehicle.__init__(self, "Mustang", "Ford", 460, 4)
        GasPowered.__init__(self, 20)

    def drive(self):
        GasPowered.drive(self, 4)

    def refuel(self):
        GasPowered.refuel(self)





