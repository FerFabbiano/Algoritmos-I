""" Corte de control: UN CORTE """
"""
    * El formato del archivo de ventas es:
    * CSV: fecha, vendedor, monto
    * Ordenado de menor a mayor por fecha y luego por vendedor
"""

# constantes 
MAX_DIA = "9999-99-99"
MAX_REG = MAX_DIA + ",xxx,0"

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


def dia_valor(registro):
    valor = int(registro[2])
    return registro[0], valor


"""
    * funcion calcula el total del dia
    *
    * pre: registro es un vector con 3 datos validos
    *      f es un archivo abierto con formato valido
    * post: acumula el total del dia
    *       devuelve el acumulado y el ultimo registro leido
"""


def total_dia(registro, f):
    dia, valor = dia_valor(registro)
    dia_actual = dia
    acum_dia   = 0
    while (dia == dia_actual and dia < MAX_DIA):
        acum_dia  += valor
        registro   = leer(f)
        dia, valor = dia_valor(registro)
        
    return acum_dia, registro


"""
    * Funcion imprimir
    *
    * pre: leyenda y dato valido, booleana False por defecto
    *
    * post: imprime la leyenda con el dato que se pase
    *       si la booleana es True imprime una separacion con espacio
"""


def imprimir(leyenda, dato, sep = False):
    print(leyenda, dato)
    if (sep):
        print ('==============================\n')
        

"""
    * funcion corte de control
    *
    * pre: recibe un archivo abierto valido
    *
    * post: realiza el corte de control x pantalla
"""
def corte_control(f):
    # Leo la primera linea
    registro = leer(f)
    suma_total = 0

    while (registro[0] < MAX_DIA):
        imprimir("Total del dia", registro[0])
        suma_dia, registro = total_dia(registro, f)
        # Aca va el corte de control
        imprimir("Acumulado", suma_dia, True)
        suma_total += suma_dia

    imprimir("\n ===== Acumulado total =", suma_total)
    

#### ========================================================

"""
    * funcion main
"""
def main():


    # Abro archivo para lectura
    f = open('ventas_diarias.txt','r')
    corte_control(f)
    f.close()


main()

    

