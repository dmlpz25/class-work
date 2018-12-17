pixza = ['pepperoni', 'extra pepperoni', 'margarita', 'mas pizza', 'mas mas pizza']
for pix in pixza: 
	print(pixza[0:3])

print("The first three items in the list are:")
for pix in pixza[:3]:
	print(pix.title())

print("Three items from the middle of the list are:")
for pix in pixza[2:3]:
	print(pix.title())

print("The last three items in the list are:")
for pix in pixza[3:6]:
	print(pix.title())

print("\nMI PIZZA, YOUR PIZZA!")

favorite_pizza=['pepperoni', 'extra pepperoni', 'margarita']
friend_pizza = favorite_pizza[:]

favorite_pizza.append("veggie lover")
friend_pizza.append('pesto')

print("My favorite pizzas are:")
for fp in friend_pizza:
	print("- " + fp)

print("\nMy friend's favorite pizzas are:")
for fp in favorite_pizza:
	print("- " + fp)

