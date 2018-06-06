# Ejercicio de parcial (matrices):
# Se cuenta con una matriz ya cargada (de enteros) de 12x4 que representa 12 sucursales de un supermercado,
# con 7 cajas. Se pide:
# •	Ver si alguna sucursal tuvo alguna caja cerrada (recaudó $0). Informar sucursal y caja (todas).
# •	Calcular el promedio de cada sucursal
# •	Armar un diccionario con: nº sucursal (clave) y valor (1 si es más grande que el promedio general, 0 si es igual
# y -1 si es menor).


def verCajaCerrada(matriz):
    ''' Guarda en un diccionario la sucursal (clave) y la caja cerrada (valor) '''
    sucursales = {}
    cajas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                sucursal = i+1
                cajas.append(j+1)
                sucursales[sucursal] = cajas
    return sucursales


def promedioSucursal(matriz):
    ''' Guarda en un diccionario el promedio de cada sucursal '''
    sucursales = {}
    cajasNoCerradas = 0
    for i in range(len(matriz)):
        totalRecaudado = sum(matriz[i])
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                cajasNoCerradas += 1
        if cajasNoCerradas != 0:
            promedio = totalRecaudado / cajasNoCerradas
            sucursal = i+1
            sucursales[sucursal] = promedio
        cajasNoCerradas = 0
    return sucursales


def promedioGeneral(matriz):
    ''' Devuelve el promedio general '''
    recaudado = 0
    cajas = 0
    for sucursal in matriz:
        recaudado += sum(sucursal)
        for caja in sucursal:
            caja += 1
    return recaudado / cajas


def diccionario(matriz):
    ''' Devuelve un diccionario con información sobre cada sucursal: 1 si el promedio de la sucursal es mayor
     al promedio general, 0 si es igual y -1 si es menor '''
    dicc = {}
    promGeneral = promedioGeneral(matriz)
    # Recorremos cada sucursal:
    for i in range(len(matriz)):
        # Para no comenzar desde la sucursal 0 sino desde la 1, hacemos:
        sucursal = i+1
        # Lo recaudado por cada sucursal y su promedio:
        recSucursal = sum(matriz[i])
        promSucursal = recSucursal / len(matriz[i])
        # Decidimos que vamos a devolver:
        if promSucursal > promGeneral:
            dicc[sucursal] = 1
        elif promSucursal < promGeneral:
            dicc[sucursal] = -1
        else:
            dicc[sucursal] = 0
    return dicc
