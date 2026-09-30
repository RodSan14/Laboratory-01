amigos = []

for amigo in range(5):
    nombre = input("Escribe el nombre del amigo " + str(amigo + 1) + ": ")
    amigos.append(nombre)

print("Tus amigos son:")
for amigo in amigos:
    print(amigo)
