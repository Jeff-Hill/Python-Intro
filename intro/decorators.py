

def interior_decorator(func):
    def add_curtains():
        func()
        print(f'now my house has purple curtains')

    return add_curtains

# def move_in():
#     print(f'My house was empty, but...')
# move_in()

# Bind returned function from interiorDecorator to a new variable
# new_house = interior_decorator(move_in)
# new_house()

def landscaper(func):
    def add_trees():
        func()
        print(f'And I planted 12 maples for shade.')
    return add_trees

@landscaper
@interior_decorator
def move_in():
    print(f'My house was empty, but...')

move_in()

# But what about passing args to the internal function?

def interior_decorator(func):
    def add_curtains(color):
        if color == "orange":
            color = "ugly-ass"
        func(color)
        print(f'now my house has {color} curtains')

    return add_curtains

@interior_decorator
def move_in(color):
    print(f'My house was empty, but...')

move_in("orange")
move_in("brown")