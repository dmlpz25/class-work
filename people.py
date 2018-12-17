# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'Javier Francisco',
    'last_name': 'Abuniz',
    'age': 29,
    'city': 'Harlingen',
    }
people.append(person)

person = {
    'first_name': 'Mercedes',
    'last_name': 'Torrez',
    'age': 29,
    'city': 'San Antonio',
    }
people.append(person)

person = {
    'first_name': 'Yvette',
    'last_name': 'Iribe',
    'age': 29,
    'city': 'Los Angles',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")