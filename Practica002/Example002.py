import random

num_secret = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número (del 1 al 10): "))

    if intento == num_secret:
        print("¡Felicidades! Adivinaste el número")
        break
    else:
        print("Intenta de nuevo")
