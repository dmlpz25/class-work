numbers = list (range(1,20))
for number in numbers:
	print (number) 

million = list (range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1,21,2))
for odd in odd_numbers:
	print(odd)

threes= list(range(3,31,3))
for tres in threes:
	print(tres)

cubes = []
for number in range(1,11):
	cube = number**3
	cubes.append(cube)

for cube in cubes:
	print(cube)

print("\n4-9")

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
	print(cube)

