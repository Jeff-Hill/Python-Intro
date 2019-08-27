

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Headache"] = "The feeling you get when you're stuck on a code problem"
word_definitions["Elation"] = "The feeling you get when you finally get your code to work"
word_definitions["Satisfaction"] = "The feeling you get as you finish a practice exercise"




"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["Awesome"])
print(word_definitions["Headache"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f'The definition of {key} is {value}')


