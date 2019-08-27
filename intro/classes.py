# Classes are a series of instructions in Python to create an object
# All objects will have attributes and/or behaviors

# Steps to creating a class
# 1. Give it a name
class Book:
    def __str__(self):
        return self.title

    def __init__(self, title, author, year_published, publisher):
        # Self equals the object you created
        # Establish the properties of each book with a default value
        # These are attributes
        self.title = title
        self.publisher = publisher
        self.author = author
        self.current_page = 1
        self.year_published = year_published
        self.currently_reading = False

# Methods "behaviors" we want on the object Book

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page

mockingbird = Book("To Kill A Mockingbird", "Harper Lee", 1960, "J.B. Lippincott & Co")
# print(mockingbird)
# mockingbird.title = "To Kill A Mockingbird"
# mockingbird.author = "Harper Lee"
# mockingbird.year_published = 1960
# mockingbird.publisher = "J.B. Lippincott & Co"

ivanhoe = Book("Ivanhoe", "Sir Walter Scott", 1934, "Dead Poets Society")

for attr, value in mockingbird.__dict__.items():
    print(f'{attr}: \n{value}\n')

print(mockingbird.currently_reading)
mockingbird.start_reading()
print(mockingbird.currently_reading)
mockingbird.stop_reading(34)
mockingbird.start_reading()
mockingbird.stop_reading(89)
mockingbird.start_reading()

# Create a book as a dictionary
book = {
    "title": "Steve",
    "author": "Joe",
    "year_published": 2019
}

book["author"]
