stuff = ["name", "age", "address", "phone"]

for foo in stuff:
    print(foo.capitalize())

# Create a new list using map
cap_stuff = list(map(lambda x: x.capitalize(), stuff))
print("map syntax", cap_stuff)

# Simpler syntax to accomplish the same result

cap_stuff = [word.capitalize() for word in stuff]

print("simpler syntax", cap_stuff)

profile = {
    "name": "Fred",
    "age": 34,
    "address": "123 Sesame St."
}

for key, value in profile.items():
    print(f'The key is {key}. The value is {value}')

# Take a dictionary and turn it into a list of strings
profile_string = [f"The key is {key}. The value is {value}" for key, value in profile.items()]
print("profile string", profile_string)