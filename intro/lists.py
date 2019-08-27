import random
my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

# """
# Print a message to the console indicating whether each value of
# `number` is in the `my_randoms` list.
# """
# for number in range(1, 6):

# compare each number in the range 1-10 to the my_randoms list
# set the initial boolean to false, loop through my_randoms,
# if the newly generated number == a number in my_randoms change
# the boolean to = True, then run the conditional to determine what to print
for number in range(1, 10):
    value = False
    for ran_number in my_randoms:
        if number == ran_number:
            value = True
    if value == True:
        print(f'my_randoms list contains:', number)
    else:
        print(f'my_randoms list does not contain:', number)