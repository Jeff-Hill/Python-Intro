import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Jeff"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories


    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime("%x")

    def purchase(self, owner):
        self.owner = owner




