# Create a tuple named zoo that contains 10 of your favorite animals.
# Find one of your animals using the tuple.index(value) syntax on the tuple.
zoo = ("gorilla", "zebra", "giraffe", "lion", "tiger", "parrot", "snake", "elephant", "rhino", "monkey")
print(zoo.index("gorilla"))

# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "giraffe"
if animal_to_find in zoo:
# Print that the animal was found
    print("Animal is in your zoo")
else:
    print("Animal is not in your zoo")

# You can reverse engineer (unpack) a tuple into another tuple
# with the following syntax.
children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple,
# and print them to the console.
print("assign zoo to variable and print", zoo)
(a, b, c, d, e, f, g, h, i, j) = zoo
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

# Convert your tuple into a list.
zoo_list = list(zoo)
print("convert tuple to a list", zoo_list)

# Use extend() to add three more animals to your zoo.
zoo_list.extend(["lizard"])
zoo_list.extend(["ostrich"])
zoo_list.extend(["alligator"])
print("zoo with 3 new animals", zoo_list)

# OR us append to add 3 animals using only a string
zoo_list.append("fish")
zoo_list.append("otter")
zoo_list.append("kangaroo")


# Convert the list back into a tuple.
zoo_tuple = tuple(zoo_list)
print("zoo tuple", zoo_tuple)
