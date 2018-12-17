mi_comida = ['tacos', 'pupusa', 'tortillas']
amigos_comida = mi_comida[:]

mi_comida.append("frijoles")
amigos_comida.append ('flautas')  

print('\nMy favorite comidas are:')
for mi in mi_comida:
	print("- " + mi)

print('\nMis amigos comidas favoritas:')
for amigos in amigos_comida:
	print("- " + amigos)

