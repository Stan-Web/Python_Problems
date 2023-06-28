"""
Algoritmo 2:

Tres amigos desean crear una empresa de desarrollo de software. Dado que se debe realizar
una inversión inicial para adquisición de muebles y equipo, alquiler de espacio fisico, pago
de impuestos entre otros, deberán juntar un capital inicial para constituir la empresa. Cada
uno tendrá un porcentaje de participación en la empresa de acuerdo con el valor que aporte
para este capital inicial. Escribir un algoritmo que lea la cantidad de dinero que uno de los
futuros socios aportará la empresa, determine y visualice el porcentaje de participación de
cada uno de estos en la empresa.
"""




# Se pide la cantidad de dinero que aportaran los socios
socio1 = float(input("Ingrese la cantidad del primer socio: "))


socio2 = float(input("Ingrese la cantidad del segundo socio: "))


socio3 = float(input("Ingrese la cantidad del tercer socio: "))

# Se calcula el capital inicial como la suma de los aportes de los tres socios
capital_inicial = socio1 + socio2 + socio3

# Calculo el porcentaje
porcentaje1 = socio1 / capital_inicial * 100
porcentaje2 = socio2 / capital_inicial * 100
porcentaje3 = socio3 / capital_inicial * 100


Porcentaje = 100 - (porcentaje1 + porcentaje2 + porcentaje3)
porcentaje3 += Porcentaje
porcentajeTotal = porcentaje1 + porcentaje2 + porcentaje3
# Se imprime el porcentaje de participación de cada socio
print(f"El socio 1 tiene una partcipacion del {porcentaje1:.2f}%")
print(f"El socio 2 tiene una partcipacion del {porcentaje2:.2f}% ")
print(f"El socio 3 tiene una partcipacion del{porcentaje3:.2f}% ")
# al igual que en el anterior use ese codigo para mostra menos decimales

