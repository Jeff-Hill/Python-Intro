import datetime

class City:
    def __init__(self, name, mayor):
        self.name = name
        self.mayor = mayor
        self.date_established = ""
        self.buildings = list()


    def add_building(self, building):
        self.buildings.append(building)

    def established(self):
        self.date_established = datetime.datetime.now().strftime("%x")





