def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def operaciones_basicas():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == "+":
        resultado = suma(num1, num2)
    elif operacion == "-":
        resultado = resta(num1, num2)
    elif operacion == "*":
        resultado = multiplicacion(num1, num2)
    elif operacion == "/":
        resultado = division(num1, num2)
    else:
        print("Operación inválida")
        return

    print("El resultado es:", resultado)

operaciones_basicas()
