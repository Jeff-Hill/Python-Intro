class ChargingStation:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        try:
            if vehicle.battery_level > -1 and vehicle.battery_capacity > -1:
                self.__vehicles.append(vehicle)
        except AttributeError:
                print (f'You cannot send any non-electric powered vehicles here')