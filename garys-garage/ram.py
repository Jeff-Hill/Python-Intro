from vehicle import Vehicle
from gasPowered import GasPowered

#  Create a Dodge Ram class
    # * `manufacturer` attribute
    # * `model` attribute
    # * `fuel_capacity` attribute
    # * `gas_level` attribute
    # * `horsepower` attribute
    # * `wheel_count` attribute
    # * `drive()` method lowers `gas_level` by 4 each time it is invoked
    # * `refuel()` method method sets `gas_level` to `fuel_capacity` value

class Ram(Vehicle, GasPowered):
    def __init__(self):
        Vehicle.__init__(self, "Ram", "Dodge", 395, 4)
        GasPowered.__init__(self, 26)

    def drive(self):
        Vehicle.drive(self, 4)

    # def refuel(self):
    #      GasPowered.drive = (self, 6)