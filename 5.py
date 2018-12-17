car = 'subaru' 
print("is car=='subaru'? I predict True.")
print(car =='subaru')

print ("\nIs car == 'audi'? I predict False.")
print (car =='audi')

print("\nSwitched to using Terminal and sublime to finish part A.")

aliencolor=['yellow']
if aliencolor == ['yellow']:
	print ("Player just earned 5 points! Nice job!")

aliencolor =['green']
if aliencolor == 'red':
	print("Player earned 5 more points!")

aliencolor = 'green'
if aliencolor == 'green':
	print("Player earned 5 pts for shooting a green alien!")
else:
	print('Player earned 10 pts')

aliencolor='green'
if aliencolor == 'yellow':
	print("Player earned 5 points!")
else:
		print("Player earned 10 points!")

print("\nAlien Color #3")

aliencolor= 'red'
if aliencolor == "green":
	print("Earned 5pts")
elif aliencolor == 'yellow':
	print("Earned 10 pts")
else:
	print("Earned 15 pts")

print("5-6 Stages of Life")

age = ['18']

if age > ['2']:
	print('\nBaby')
elif age > ['4']:
	print('\nToddler')
elif age < ['12']:
	print('\nKid')
elif age < ['20']:
	print('Teen')
elif age < ['65']:
	print('\nADULT!')
else:
	print('\nWise Elder')

print ("favorite fruit/fruit cup")
favfruit = ['mango','cucumber','jicama']
if 'mango' in favfruit:
	print("Yes,")
if 'cucumber' in favfruit:
	print("that too")
if 'jicama' in favfruit:
	print("add Tijan, SAL y Limon, please!")
if 'strawberries' in favfruit:
	print("no thx")
if 'oranges' in favfruit:
	print("nah!")

print("hello admin 5-8")

usernames = ['Admin', 'Bobby', 'Stella', 'Guest', 'Maya']
for username in usernames:
	if username == 'Admin':
		print("Hello Admin, would you like to see a status report?")
	else:
		print("Hello " + username + " ,thank you for logging in again.")

print("5-9 No username")

usernames=[]
if usernames:
	for username in usernames:
		if username == 'Admin':
			print("Hello Admin, would you like to see a status report?")
		else:
			print("Hello " + username + " ,thank you for logging in again.")
else:
    print("We need to find some users!")

print("5-10 Checking Usernames")

current_users = ['Kelly', 'EMMA', 'bobby', 'Mike', 'Rodney']
new_users = ['sara', 'chris', 'Mike', 'EMMA', 'Tony']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

print("5-11")

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")