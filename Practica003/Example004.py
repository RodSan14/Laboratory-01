def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

print(" CALCULADORA ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Elige una operación: "))
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == 1:
    print("Resultado:", sumar(num1, num2))

if opcion == 2:
    print("Resultado:", restar(num1, num2))

if opcion == 3:
    print("Resultado:", multiplicar(num1, num2))

if opcion == 4:
    print("Resultado:", dividir(num1, num2))

if opcion < 1 or opcion > 4:
    print("Opción no válida")
