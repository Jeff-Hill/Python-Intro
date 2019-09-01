# @read_only_properties('social_security', 'birth_date', 'insurance_number')

class Patient:
    def __init__(self, social_security, birth_date, insurance_number, address, first, last):
        self.__social_security = social_security
        self.__birth_date = birth_date
        self.__insurance_number = insurance_number
        self.address = address
        self.__first_name = first
        self.__last_name = last

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @address.setter
    def address(self, address):
        if isinstance(address, str):
            self.__address = address
        else:
            print("Must be a string")

    @property
    def social_security(self):
        try:
            return self.__social_security
        except AttributeError:
            return 0

    @property
    def birth_date(self):
        try:
            return self.__birth_date
        except AttributeError:
            return 0

    @property
    def insurance_number(self):
        try:
            return self.__insurance_number
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return f'{self.__first_name} {self.__last_name}'
        except AttributeError:
            return 0

Jeff = Patient("546-32-4567", "2.16.78", "435324567", "2339 Devonshire Dr", "Jeff", "Hill")
print(Jeff)
# Jeff.insurance_number = "123-45-4534"
# Jeff.address = "123 Maint St."
print(Jeff.social_security)
# print(Jeff.first_name)
print(Jeff.full_name)
print(Jeff.address)
Jeff.address = "123 Maint St."
print(Jeff.address)

