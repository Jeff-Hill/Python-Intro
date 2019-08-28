# Create a function called calc_dollars. In the function body,
# define a dictionary and store it in a variable named piggyBank.
# The dictionary should have the following keys defined.
def calc_dollars():
    piggyBank = {
        "quarters": 100,
        "nickles": 50,
        "dimes": 75,
        "pennies": 200
    }
    for (key,value) in piggyBank.items():
            if(key == "quarters"):
                quarters = (value*0.25) * 1
                print(f'Value in dollars is: ${quarters}')
            elif(key == "nickles"):
                nickles = (value*0.05) * 1
                print(f'Value in dollars is: ${nickles}')
            elif(key == "dimes"):
                dimes = (value*0.10) * 1
                print(f'Value in dollars is: ${dimes}')
            elif(key == "pennies"):
                pennies = (value*0.01) * 1
                print(f'Value in dollars is: ${pennies}')
    dollarAmount = [quarters, nickles, dimes, pennies]
    total= sum(dollarAmount)
    print(f'The total dollar amount is: ${total}')

calc_dollars()
# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

# piggyBank = {
#     "pennies": 342,
#     "nickels": 9,
#     "dimes": 32
# }
# Once you have given yourself a large stash of coins in your piggybank,
# look at each key and perform the appropriate math on the integer value to determine
# how much money you have in dollars. Store that value in a variable named dollarAmount and print it.
# Given the coins shown above, the output would be 7.07 when you call calc_dollars()