print("** MENÚ DE COMIDA **")
print("1. Pizza")
print("2. Hamburguesa")
print("3. Tacos")
print("4. Ensalada")

opcion = int(input("Elige una opción: "))

menu = {
    1: "Pizza",
    2: "Hamburguesa",
    3: "Tacos",
    4: "Ensalada"
}

if opcion in menu:
    print("Elegiste", menu[opcion])
else:
    print("Opción no válida")
