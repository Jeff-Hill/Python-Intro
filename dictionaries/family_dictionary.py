# Dictionary Challenge Exercise

# Define a dictionary that contains information about several
# members of your family. Use the following example as a template.
my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

# Using a dictionary comprehension, produce output that looks like
# the following example.

for fam_member, details in my_family.items():
        print(f'{details["name"]} is my {fam_member} and is {str(details["age"])} years old')
# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

# # Using a comprehension
# fam_stuff = {v["name"] + " is my " + k + " and is" + str(v["age"]) + " year old." for (k, v) in my_family.items()}

# for person in fam_stuff:
