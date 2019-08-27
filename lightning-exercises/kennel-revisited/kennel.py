animals_in_kennel = [
    {
        "id": 1,
        "breed": "German Shepherd",
        "age": 3,
        "name": "Jack"
    },
    {
        "id": 2,
        "breed": "Siamese",
        "age": 9,
        "name": "Shy"
    },
    {
        "id": 3,
        "breed": "Labradoodle",
        "age": 5,
        "name": "Avett"
    },
    {
        "id": 4,
        "breed": "Shnauzer",
        "age": 1,
        "name": "Gypsy"
    },
]

animals = list(map(lambda Key: Key, animals_in_kennel))
print(animals)

for animal in animals_in_kennel:
    for k,v in animal.items():
        print(f'Key "{k}" = {v}')

