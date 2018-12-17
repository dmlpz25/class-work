favorite_numbers = {
    'bobby': [12, 4, 89],
    'maya': [5, 1, 15],
    'guest': [10, 30, 13],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))