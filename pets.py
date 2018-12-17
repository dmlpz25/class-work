# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'dog',
    'name': 'Maya',
    'owner': 'Bobby J',
    'weight': 15,
    'eats': 'Dog Food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Stella',
    'owner': 'Diane',
    'weight': 15,
    'eats': 'Dog Food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Guest',
    'owner': 'Diane',
    'weight': 20,
    'eats': 'Dog Food',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))