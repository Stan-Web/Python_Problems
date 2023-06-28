import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

def calcular_area_figura():
    figura = input("Ingrese la figura (círculo, triángulo o cuadrado): ")

    if figura == "círculo":
        radio = float(input("Ingrese el radio: "))
        area = calcular_area_circulo(radio)
    elif figura == "triángulo":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = calcular_area_triangulo(base, altura)
    elif figura == "cuadrado":
        lado = float(input("Ingrese el lado: "))
        area = calcular_area_cuadrado(lado)
    else:
        print("Figura inválida")
        return

    print("El área es:", area)

calcular_area_figura()
