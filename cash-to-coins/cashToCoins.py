# Now do the reverse. Convert the dollar amount into the coins that
# make up that dollar amount. The final result is an object with the
# correct number of quarters, dimes, nickels, and pennies.

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here

quarters = round(dollarAmount/.25)
print("Quarters", quarters)
dollarAmount = dollarAmount%.25
dimes = round(dollarAmount/.10)
print("Dimes", dimes)
dollarAmount = dollarAmount%.10
nickels = round(dollarAmount/.05)
print("Nickels", nickels)
dollarAmount = dollarAmount%.05
pennies = round(dollarAmount/.01)
print("Pennies", pennies)
dollarAmount = dollarAmount%.01

piggyBank['quarters'] = quarters
piggyBank['dimes'] = dimes
piggyBank['nickels'] = nickels
piggyBank['pennies'] = pennies
print(f'The piggy bank has {piggyBank}')



# That should produce the following output.

# >>> print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }