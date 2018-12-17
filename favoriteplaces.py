favorite_places = {
    'Bobby': ['Oaxaca, Mex', 'Las Vegas', 'pagosa spring, co'],
    'Diane': ['San Francisco del Valle, Honduras', 'Chiapas, Mex'],
    'Denise': ['Arizona', 'the playground', 'San Antonio, Texas']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())