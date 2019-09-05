from .flower import Flower
from organic import Organic

class Rose(Flower, Organic):
    def __init__(self, color):
        self.color = color
        Flower.__init__(self, "Rose", 7)
        Organic.__init__(self)
    pass



