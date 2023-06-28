# Seguimiento de Medicamentos en Sucursales
# Descripción del problema:
# Escribe un programa en Python que realice el seguimiento de los medicamentos consumidos en diferentes sucursales y calcule el porcentaje de medicamentos consumidos en cada una. El programa debe recibir como entrada el número de sucursales, el número de medicamentos y los datos correspondientes a las mediciones de presión arterial y la sucursal.

# Especificaciones del programa:
# El programa debe cumplir con las siguientes especificaciones:

# Solicitar al usuario el número de sucursales (n) y el número de medicamentos (m)
n = int(input("Ingrese el número de sucursales: "))
m = int(input("Ingrese el número de medicamentos: "))

# Crear las listas de sucursales, medicamentos y medicamentos consumidos
sucursales = list(range(1, n + 1))
medicamentos = list(range(1, m + 1))
med_consumidos = [0] * n
porcentajes = [0] * n

# Solicitar los identificadores de los medicamentos al usuario
for i in range(m):
    medicamentos[i] = int(input("Ingrese el identificador del medicamento: "))



# Registrar las mediciones de presión arterial y la sucursal

for _ in range(m):

    sucursal, sistolica, diastolica = map(int, input("Ingrese la sucursal, la presión arterial sistólica y la presión arterial diastólica: ").split())
   
        # Calcular la dosis correspondiente según las mediciones de presión arterial
    if sistolica < 80 and diastolica < 60:
            dosis = 5
    elif 80 <= sistolica < 120 and 60 <= diastolica < 80:
            dosis = 0
    elif 130 <= sistolica < 140 and 85 <= diastolica < 90:
            dosis = 2
    elif 140 <= sistolica < 160 and 90 <= diastolica < 100:
            dosis = 5
    elif 160 <= sistolica < 180 and 100 <= diastolica < 110:
            dosis = 10
    elif sistolica >= 180 and diastolica >= 110:
            dosis = 30
    elif 140 <= sistolica < 180 and diastolica < 90:
            dosis = 20
    else:
        continue

    if sucursal > n:
            continue


    posicion = sucursales.index(sucursal)
    med_consumidos[posicion] -= dosis



# Calcular el porcentaje de medicamentos consumidos en cada sucursal
for i in range(n):
    porcentajes[i] = 1 - (med_consumidos[i] / len(medicamentos))

maximo = max(med_consumidos)
minimo = min(med_consumidos)
posmax = med_consumidos.index(maximo) + 1
posmin = med_consumidos.index(minimo) + 1

# Imprimir la posición y cantidad mínima y máxima de medicamentos consumidos
print("Posición y cantidad mínima de medicamentos consumidos:", posmin, minimo)
print("Posición y cantidad máxima de medicamentos consumidos:", posmax, maximo)

# Imprimir el porcentaje de medicamentos consumidos en cada sucursal
for sucursal, porcentaje in zip(sucursales, porcentajes):
    print("Sucursal", sucursal, "- Porcentaje de medicamentos consumidos: {:.2%}".format(porcentaje))

