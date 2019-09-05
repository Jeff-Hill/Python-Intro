from . import Arrangement

class ValentinesDay(Arrangement):
    def __init__(self):
        Arrangement.__init__(self)


    def enhance(self, flower):
            try:
                if flower.organic == False:
                    self.__flowers.append(flower)
            except AttributeError:
                print(f'You cannot add organic flowers to this arrangement')