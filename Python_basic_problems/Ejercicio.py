def jugar_con_operadores():
    a = 5
    b = -a
    c = a + 1
    d = b - 1

    resultado = (a * b) + (c / d) - (a % d)

    print("Resultado =", resultado)

    x = 10
    y = 5
    z = 8

    condicion = (x == y) or (x > z)
    print("Condición =", condicion)

    condicion = (x != y) and (x <= z)
    print("Condición =", condicion)

    valor = 7

    resultado_terciario = 10 if valor > 5 else 20
    print("Resultado ternario =", resultado_terciario)

jugar_con_operadores()

