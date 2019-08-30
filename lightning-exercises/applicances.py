# Add 3 indispensable appliances to this tuple
Appliances = ("oven", "refrigerator", "coffeemaker", "ricecooker")
new_appliances = list(Appliances)
new_appliances.append("can opener")
new_appliances.append("toaster")
new_appliances.append("mixer")
new_appliances.extend(["steamer", "grill"])
Appliances = tuple(new_appliances)
print(Appliances)
# Don't need to define a new variable of new_appliances. Can just keep re-assigning
# values to appliances
Appliances = ("oven", "refrigerator", "coffeemaker", "ricecooker")
Appliances = list(Appliances)
Appliances.append("can opener")
Appliances.append("toaster")
Appliances.append("mixer")
Appliances.extend(["steamer", "grill"])
Appliances = tuple(Appliances)
print(Appliances)


