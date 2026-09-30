numeros = []

for i in range(5):
    numero = int(input("Escribe el número " + str(i + 1) + ": "))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print("El número mayor es:", mayor)
print("El número menor es:", menor)
