"""
Algoritmo 1

Desarrolle un algoritmo que permita liquidar el valor de sus vacaciones. Para esto el
algoritmo debe solicitar el salario mensual y la cantidad de días trabajados y aplicar la
siguiente fórmula:

Vacaciones= (salario * dias trabajados)/ 720
"""

#se piden los datos necesarios para realizar la operacion
salarioMensual=float(input('Ingrese su salario mensual: '))
diasQueTrabajo=int(input('Ingrese cuantos dias trabajo: '))
# se realiza la operacion para obtener el valor de las vacaciones
Vacaciones=(salarioMensual*diasQueTrabajo)/720
#Se imprime  el Valor de las vacaciones 
print(f'El valor de sus Vacaciones es de: ${ Vacaciones: .3f} USD' )
#el codigo que use para mostrar menos decimales lo investigue en google porque no queria que el resultado mostrara tantos decimales