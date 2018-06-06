""" Corte de control: DOS CORTES """
"""
    * El formato del archivo de ventas es:
    * CSV: fecha, vendedor, monto
    * Ordenado de menor a mayor por fecha y luego por vendedor
    *
    * Primer corte (mas interno) por vendedor
    * Segundo corte (mas externo) por dia
"""

# constantes 
MAX_DIA = "9999-99-99"
MAX_REG = MAX_DIA + ",xxx,0"
ARCHIVO = "ventas_diarias.txt"

# funciones ====================================================

"""
    * funcion leer archivo - lee una línea del archivo
    *
    * pre: f es un archivo abierto con lineas con formato valido
    *
    * post: devuelve la línea como una lista de 3 valores
    *       dia, cliente, valor
    *       si llegó al fin de archivo devuelve MAX_REG
"""


def leer(f):
    linea = f.readline()
    if (not(linea)):
        linea = MAX_REG
    linea = linea.rstrip()
    return linea.split(',')



"""
    * funcion que recibe un registro y devuelve el dia y el valor
    *
    * pre: recibe un registro valido con tres campos
    *
    * post: pasa el valor a entero
    *       devuelve el dia de la operacion y el monto
"""


def dia_vendedor_valor(registro):
    valor = int(registro[2])
    return registro[0], registro[1], valor


"""
    * Funcion omprimir
    *
    * pre: leyenda y dato valido, booleana False por defecto
    *
    * post: imprime la leyenda con el dato que se pase
    *       si la booleana es True imprime una separacion con espacio
"""


def imprimir(leyenda, dato, sep = False):
    print(leyenda, dato)
    if (sep):
        guion = "=" * 55
        print (guion,'\n')
        

"""
    * total por cliente
    *
    * pre: recibe un registro valido y un archivo abierto
    *
    * post: acumula y devuelve el total por vendedor, el vendedor y el registro actual
"""


def total_vendedor(registro, f):
    dia, vendedor, valor        = dia_vendedor_valor(registro)
    dia_actual, vendedor_actual = dia, vendedor
    acum_vendedor = 0
    while (vendedor == vendedor_actual and dia == dia_actual and dia < MAX_DIA):
        acum_vendedor  += valor
        registro        = leer(f)
        dia, vendedor, valor   = dia_vendedor_valor(registro)
        
    return acum_vendedor, vendedor_actual, registro



"""
    * total por dia
    *
    * pre: recibe un registro valido y un archivo abierto
    *
    * post: acumula y devuelve el total por dia y el registro actual
"""


def total_dia(registro, f):
    dia, vendedor, valor = dia_vendedor_valor(registro)
    dia_actual = dia
    vendedor_actual = vendedor
    acum_dia   = 0
    while (dia == dia_actual and dia < MAX_DIA):
        acum_vendedor, vendedor_procesado, registro = total_vendedor(registro, f)
        leyenda = "   --- Acumulado por vendedor: " + vendedor_procesado + " - $"
        imprimir(leyenda, acum_vendedor)
        acum_dia  += acum_vendedor
        dia = registro[0]
        
    return acum_dia, registro


"""
    * funcion que hace el corte de control global
    *
    * pre: recibe un archivo bien formado, abierto
    *
    * post: genera e imprime por pantalla el corte de control
"""


def corte_control(f):
    # Leo cada una de las lineas
    registro = leer(f)
    acum_total = 0

    while (registro[0] < MAX_DIA):
        imprimir("\nTotal del dia", registro[0])
        acum_dia, registro = total_dia(registro, f)
        acum_total = acum_total + acum_dia
        imprimir("  Acumulado por día", acum_dia, True)

    imprimir("\n====== Acumulado total =", acum_total)


#### =================================================


"""
    * funcion main
"""


def main():
    # Abro archivo para lectura
    f = open(ARCHIVO,'r')
    corte_control(f)
    f.close()

    
main()

