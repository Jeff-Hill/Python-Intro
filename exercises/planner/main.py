from building import Building
from city import City

# import datetime

eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.purchase("Donald Duck")
eight_hundred_eighth.construct()
print(f'{eight_hundred_eighth.address} was purchased by {eight_hundred_eighth.owner} on {eight_hundred_eighth.date_constructed} and has {eight_hundred_eighth.stories} stories')

home = Building("2339 Devonshire Dr.", 2)
home.purchase("Mickey Mouse")
home.construct()
print(f'{home.address} was purchased by {home.owner} on {home.date_constructed} and has {home.stories} stories')

school = Building("301 Plus Park Blvd", 5)
school.purchase("Goofy")
school.construct()
print(f'{school.address} was purchased by {school.owner} on {school.date_constructed} and has {school.stories} stories')


Nashville = City("Nashville", "Jeff")
Nashville.established()
Nashville.add_building(home)
Nashville.add_building(school)
Nashville.add_building(eight_hundred_eighth)
for building in Nashville.buildings:
    print(f'Nashville has a {building.stories} story building at {building.address} that was built by {building.owner} on {building.date_constructed}.')

# for building in Nashville.__dict__.items():
#         print({building.Building.owner})



