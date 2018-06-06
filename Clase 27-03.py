def solicitarValor():
    """solicita el ingreso de un valor numerico, asegurando que el mismo sea mayor o igual a cero."""
    valor = input("Valor: ")
    while not (valor.isdigit()):
        print("Error, debe ingresar un numero mayor o igual a 0")
        valor = input("Valor: ")
    return int(valor)


def factorial(n):
    """Calcula el factorial del valor recibido, que debe ser mayor o igual a cero."""
    resultado = 1
    for i in range(2, n+1):
        resultado = resultado * i
    return resultado

#valor_ingresado = solicitarValor()
#print("Factorial: ", factorial(valor_ingresado))



def solicitar_Valor(mensaje,min,max):
    """Solicita el ingreso de un valor numerico asegurando que el mismo este entre los limites pasados como parametros"""
    valor = input(mensaje)
    while not(valor.isdigit()) or int(valor) < min or int(valor) > max:
        print("Error! Debe insgresar un valor entre {0} y {1}".format(min, max))
        valor = input(mensaje)
    return int(valor)


def cantidadDiaMes(mes, año):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if (año % 400 == 0) or ((año % 4 == 0) and (año % 100 != 0)):
            return 29
        else:
            return 28


def añobisiesto(mes, año):
    if (mes == 2) and (año % 400 == 0) or ((año % 4 == 0) and (año % 100 != 0)):
        return 29
    else:
        return 28




mes_ingresado = solicitar_Valor("Mes: ", 1, 12)
año_ingresado = solicitar_Valor("Año:", 0, 2500)
print("Cantidad de dias: ", cantidadDiaMes(mes_ingresado, año_ingresado))











