from mustang import Mustang
from ram import Ram
from leaf import Leaf
from crosstrek import CrossTrek
from pumpstation import PumpStation
from chargingstation import ChargingStation

ram = Ram()
must = Mustang()
tree = Leaf()

gas_pump_station = PumpStation()
electric_charging_station = ChargingStation()

gas_pump_station.add_vehicle(ram)
gas_pump_station.add_vehicle(must)
electric_charging_station.add_vehicle(tree)

the_hotness = Mustang()
the_hotness.refuel()
the_hotness.drive()

buzz = Leaf()
buzz.refuel()
buzz.drive()

buzz_growl = CrossTrek()
buzz_growl.refuel()
buzz_growl.drive()



