def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def calcular_factorial():
    num = int(input("Ingrese un número: "))
    resultado = factorial(num)
    print("El factorial de", num, "es:", resultado)

calcular_factorial()
