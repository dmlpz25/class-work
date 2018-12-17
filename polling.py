favorite_languages = {
    'Katya': 'python',
    'Lena': 'c',
    'Barry': 'ruby',
    'Diane': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['Katya', 'Lena', 'Barry', 'Diane']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")

