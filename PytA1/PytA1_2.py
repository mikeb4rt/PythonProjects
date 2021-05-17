def calc():
    num1 = int(input("Introduzca 1 numero entre 1-100"))
    num2 = int(input("Introduzca otro numero entre 1-100"))

    print("""             1- Sumar numeros
             2- Restar numeros
             3- Multiplicar numeros
             4- Dividir dumeros""")
    opcio = int(input("Elija una opcion"))

    if opcio == 1:
        result = num1 + num2
    elif opcio == 2:
        result  = num1 - num2
    elif opcio == 3:
        result = num1 * num2
    elif opcio == 4:
        result = num1 / num2
    else:
        result = "opcio no valida"
    return result
print(calc())