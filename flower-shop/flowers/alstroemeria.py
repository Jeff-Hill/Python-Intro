from .flower import Flower
from organic import Organic

class Alstroemeria(Flower, Organic):
    def __init__(self, color):
        self.color = color
        Flower.__init__(self, "Alstroemeria", 7, False)
