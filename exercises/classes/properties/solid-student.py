# Define a Python class named Student. This class will have 5 properties.
# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)

class Student:

# Define getters for all properties.
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0
# Define a setter for all but the read only property.
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name
# Ensure that only the appropriate value can be assigned to each.

        else:
            print("Must be a string")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Must be a string")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("Must be a number")

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @cohort.setter
    def cohort(self, cohort):
        if isinstance(cohort, int):
            self.__cohort = cohort
        else:
            print("Must be a number")
# The full name property should return first name and last name separated by a space. It's value cannot be set.

    @property
    def full_name(self):
        try:
            return self.__full_name
        except AttributeError:
            return f'{self.first_name} {self.last_name}'
# Use the __str__ and __repr__ magic methods on your class to specify what an object's string
# representation should be. It's just like the toString() method in JavaScript.
    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old and is in cohort {self.cohort}.'

Jeff = Student()
Jeff.first_name = "Jeff"
Jeff.last_name = "Hill"
Jeff.age = 21
Jeff.cohort = 33
print("full name =", Jeff.full_name)
# Change your class so that any objects created from it will be
# rerpesented as strings in the following format.
# Mike Ellis is 35 years old and is in cohort 39
print(Jeff)




