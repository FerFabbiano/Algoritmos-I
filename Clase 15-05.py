""" CORTE DE CONTROL """

""" ARCHIVOS """

# Persistencia de datos --> puedo guardar los datos
# Desventaja: menos eficiente
# Tipos(la diferencia es como guardo los datos): texto(si guardo un "8", se me va a guardar como string) --> csv,
# binario(complemento A 2, lo guarda con un formato distinto, son los mas eficientes) --> 8
# OPERACIONES: Merge --> unir datos de diferentes archivos,
# Apareo --> modifico un archivo mediante el cruce con uno nuevo
# Corte de control --> Calcula subtotales (puedo guardarlo en un nuevo archivo o mostrarlo en pantalla)

""" CORTE DE CONTROL """

# 1°) Debe estar el archivo ordenado
# Debo recorrer el archivo línea por línea
# Con rstrip() le quito el \n


fzen = open("C:/Users/Fernando/Desktop/ArchivoPrueba.csv", "r+")


def leerArchivo(archivo):
    d = {}
    for linea in archivo:
        linea = linea.strip("\n")
        linea = linea.split(",")
        if linea[0] not in d:
            d[linea[0]] = int(linea[2])
        else:
            d[linea[0]] += int(linea[2])
    print(d)
    for x in d.items():
        print(x)


#leerArchivo(fzen)
#print("10\n")
#print("hola")

"""

Algoritmo Modelo de corte de control


def leer_info(ejs, default):
            linea = ejs.readline()
            return  linea if linea    else   default

with open('movimientos.txt', 'rt') as movs:
        linea = leer_info(movs, '999999,0')
        nro_cta, importe = linea.rstrip().split(',')
        max = '999999'
        print (nro_cta, importe)
        total = 0
        while nro_cta != max:
            cta_ant = nro_cta
            tot_cta = 0
            print ('cta',cta_ant)
            print ('importe',importe)
            while nro_cta == cta_ant and nro_cta != max:
                print (importe)
                tot_cta+=int(importe)
                print (nro_cta, importe)
                linea = leer_info(movs, '999999,0')
                nro_cta, importe = linea.rstrip().split(',')
            print ('cierre')
            print ('El total de la cuenta {} es {}:'.format(cta_ant, tot_cta))
            total += tot_cta
print ('Total Gral:', total)


"""