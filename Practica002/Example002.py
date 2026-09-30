import random

numero_secreto = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número (del 1 al 10): "))

    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número")
        break
    else:
        print("Intenta de nuevo")

