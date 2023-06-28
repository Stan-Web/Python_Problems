def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

def esta_en_peso_ideal(peso, altura):
    imc = peso / (altura * altura)
    if 18.5 <= imc <= 24.9:
        return True
    else:
        return False

def recibir_informacion_persona():
    tipo_documento = input("Ingrese el tipo de documento: ")
    numero_documento = int(input("Ingrese el número de documento: "))
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo: ")
    peso = float(input("Ingrese el peso: "))
    altura = float(input("Ingrese la altura: "))

    if es_mayor_de_edad(edad):
        print("La persona es mayor de edad")
    else:
        print("La persona no es mayor de edad")

    if esta_en_peso_ideal(peso, altura):
        print("La persona está en su peso ideal")
    else:
        print("La persona no está en su peso ideal")

recibir_informacion_persona()
