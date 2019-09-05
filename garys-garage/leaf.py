from electricPowered import ElectricPowered
from vehicle import Vehicle
#  Create a Nissan Leaf class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `battery_capacity` attribute
#     * `battery_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `battery_level` by 2 each time it is invoked
#     * `recharge()` method sets `battery_level` to `battery_capacity` value

class Leaf(Vehicle, ElectricPowered):
    def __init__(self):
        Vehicle.__init__(self, "Leaf", "Nissan", 50, 4)
        ElectricPowered.__init__(self, 45)



    def drive(self):
        ElectricPowered.drive(self, 1)
