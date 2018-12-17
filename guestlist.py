petdinner = ['Guest','Stella', 'Maya', 'Lucky']

msg="hello, " + petdinner[0].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[1].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[2].title() + " ,Who is hungry!"
print(msg)

msg="Hello, " + petdinner[3].title() + " ,Who is hungry!"
print(msg)

msg="Nah, " + petdinner[0].title() + " ,I am not hungry!"
print(msg)

del(petdinner[0])
petdinner.insert(0, 'Fendi')

msg="Hello, " + petdinner[0].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[1].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[2].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[3].title() + " ,Who is hungry!"
print(msg)

print("\nAdding Guest back and some new Doggos!!!")

petdinner.insert(4, 'Guest')
petdinner.insert(5, 'Jumper')
petdinner.append('Tom Ford')

sg="hello, " + petdinner[0].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[1].title() + " ,Who is hungry!"
print(msg)

msg="hello, " + petdinner[2].title() + " ,Who is hungry!"
print(msg)

msg="Hello, " + petdinner[3].title() + " ,Who is hungry!"

msg="Hello, " + petdinner[4].title() + " ,Who is hungry!"
print(msg)
msg="Hello, " + petdinner[5].title() + " ,Who is hungry!"
print(msg)
msg="Hello, " + petdinner[6].title() + " ,Who is hungry!"
print(msg)

print("\nI have a lot of dogs, and I love to foster dogs too!!!")

print("\nShrinking Guest List")
print("\nHello, everyone can bring two more doggos to the pet dinner party!")

popped_petdinner = petdinner.pop()
print(petdinner)
print(popped_petdinner)

petdinner.remove('Stella')
print(petdinner)

too_manydoggos = 'Stella'
print(petdinner)

print("\n" + too_manydoggos.title() + " is no longer invited, sorry!")

print("\nJumper, you are still invited")
print("\nGuest, you are still invited")





