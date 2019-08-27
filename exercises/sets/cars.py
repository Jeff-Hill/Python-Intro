# You can create a set in one of two ways.

# Using set() to create a set
languages = set()

# Using curly braces allows you to initialize the set with values
languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }

# Notice that both of those sets were constructed with some duplicate items. However, when you print out the set, the duplicates are gone.

print(languages)
{'english', 'mandarin chinese', 'portugese', 'spanish'}

# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom = {"mustang", "camaro", "challenger", "masarati"}
print("original set of cars", showroom)

# Print the length of your set.
print("length of showroom set", showroom.__len__())

# Pick one of the items in your show room and add it to the set again.
showroom.add("mustang")

# Print your showroom. Notice how there's still only one instance of that model in there.
print("set won't output duplicate items", showroom)

# Using update(), add two more car models to your showroom with another set.
new_showroom = {"lincoln", "cadillac"}
showroom.update(new_showroom)
print("updated showrooom using new set", showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.remove("lincoln")
print("set without sold card", showroom)

# Acquiring more cars
# Now create another set of cars in a variable junkyard.
# Someone who owns a junkyard full of old cars has approached you about buying the entire inventory.
# In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"pinto", "sentra", "accord", "pathfinder", "mustang", "camaro"}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
compare_auto_sets = showroom.intersection(junkyard)
print("output which cars are in both sets", compare_auto_sets)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
# print("output combined sets of cars", combine_auto_sets)
print("showroom.union", showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
showroom.discard("pathfinder")
showroom.discard("sentra")
print("discard", showroom)