from random import randrange

def crearMatriz(m, n):
    """
    Crea y devuelve una matriz de tamaño m x n con valores aleatorios.

    Parameters:
    - m (int): Número de filas de la matriz.
    - n (int): Número de columnas de la matriz.

    Returns:
    - mat (list): Matriz generada con valores aleatorios.
    """
    mat = []

    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(randrange(10))
        mat.append(fila)
    return mat

def calcularPromedio(T):
    """
    Calcula el promedio de los elementos de una matriz.

    Parameters:
    - T (list): Matriz de la cual se desea calcular el promedio.

    Returns:
    - prom (float): Promedio de los elementos de la matriz.
    """
    suma = 0
    cont = 0

    for i in range(len(T)):
        fila = T[i]
        for j in range(len(fila)):
            dato = T[i][j]
            suma = suma + dato
            cont = cont + 1
    
    prom = suma / cont

    return prom
    
def actividad2(m, n):
    """
    Realiza la actividad 2.

    Parameters:
    - m (int): Número de filas de la matriz.
    - n (int): Número de columnas de la matriz.
    """
    mat = crearMatriz(m, n)
    mat2 = []
    prom = calcularPromedio(mat)

    print("El promedio es:", prom)

    for i in range(len(mat)):
        fila = []
        for j in range(len(mat[i])):
            dato = mat[i][j]
            if dato >= prom:
                fila.append(1)
            else:
                fila.append(0)
        mat2.append(fila)

    print("Matriz original:")
    print(mat)
    print("Matriz binaria:")
    print(mat2)


