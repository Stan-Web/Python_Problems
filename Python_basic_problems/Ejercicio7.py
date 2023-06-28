import time
cant=0
print("")
print("")


while cant ==0 :
    print("")
    print("")
    time.sleep(2)
    print("""¿que operacion deseas hacer?""")
    time.sleep(2)
    print("""
    1:suma.
    2:resta.
    3:multiplicacion.
    4: division.
    5:porcentaje.
    6:apagar calculadora.""")
    time.sleep(2)
    print("")
    num=int(input("escribe el numero correspondiente a la operacion q deseas realizar:"))
    if num==1:
        print("")
        time.sleep(1)
        print("Elegiste la opcion 1;SUMA.")
        print("")
        a=int(input("Ingresa el primer digito:"))
        b=int(input("Ingresa el segundo digito:"))
        print("la suma es:",a,"+",b)
        suma=a+b
        time.sleep(2)
        print("el resultado de tu suma es:",suma)
    elif num==2:
        print("")
        time.sleep(1)
        print("Elegiste la opcion 2;RESTA.")
        print("")
        a=int(input("Ingresa el primer digito:"))
        b=int(input("Ingresa el segundo digito:"))
        print("la resta es:",a,"-",b)
        resta=a-b
        time.sleep(2)
        print("el resultado de tu resta es:",resta)
    elif num==3:
        print("")
        time.sleep(1)
        print("Elegiste la opcion 2;MULTIPLICACION.")
        print("")
        a=int(input("Ingresa el primer digito:"))
        b=int(input("Ingresa el segundo digito:"))
        print("la resta es:",a,"*",b)
        multiplicacion=a*b
        time.sleep(2)
        print("el resultado de tu multiplicacion es:",multiplicacion)   
    elif num==4:
        print("")
        time.sleep(1)
        print("Elegiste la opcion 2;DIVISION.")
        print("")
        a=int(input("Ingresa el primer digito:"))
        b=int(input("Ingresa el segundo digito:"))
        print("la resta es:",a,"/",b)
        division=a/b
        time.sleep(2)
        print("el resultado de tu division es:",division)    
    elif num==5:
        print("")
        time.sleep(1)
        print("Elegiste la opcion 2;PORCENTAJE.")
        print("")
        a=int(input("elige el valor total:"))
        b=int(input("elige el porcentaje que deseas calcular:"))
        time.sleep(2)
        porcentajes=(a*b)/100
        time.sleep(2)
        print("El porcentaje es:",porcentajes)    

    elif num==6:
        print("gracias por usar mi calculadora")
        break
    else:
        print("Esa opcion no es valida")