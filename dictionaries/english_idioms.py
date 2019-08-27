# Create a new Python file and paste the following code into it.
# At the end write a for in loop to produce the output below.

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (key, value) in idioms.items():
    # Have to use join on the values only first
    # so define a variable for what you want to use in the concatenation
    s = " "
    # then define a variable to use the join method on the values
    value_strings = s.join(value)
    # lastly print the key, value pairs using the join variable for the values
    print (f'{key}: {value_strings}')

