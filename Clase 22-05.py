"""" MERGE """

# Archivos secuenciales y ordenados por cuenta

"""

leo Mov. 1
leo Mov. 2

while not EOF1 or not EOF2    
    menor <-- menor(cta1, cta2)
    tot <-- 0
    while menor = cta1:
        total <-- tot + imp1
        leo mov1    
    while menor = cta2:
        total <-- tot + imp2
        leo mov2
    muestro total
    grabo total (en un nuevo archivo)

# Por cada archivo agrego un while

"""

""" Lee el archivo linea por linea, devuelve linea si existe, y sino lo que tiene en default. Si no devuelve nada, es 
el fin de archivo"""

movimientos1 = open("..\prueba corte de control.txt", "rt")
movimientos2 = open("..\prueba corte de control 2.txt", "rt")
max = 9999999999999999



def leer(movimientos, default):
    linea = movimientos.readline()
    #print(linea)
    return linea if linea else default


linea1 = leer(movimientos1, "max, 0")
linea2 = leer(movimientos2, "max, 0")

cta1, imp1 = linea1.rstrip().split(",")
cta2, imp2 = linea2.rstrip().split(",")

while cta1 != max or cta2 != max:
    menor = min(cta1, cta2)
    totcta = 0
    while cta1 == menor:
        #print (imp1)
        #imp1 = int(imp1)
        totcta += int(imp1)
        linea1 = leer(movimientos1, "max,0")
        cta1, imp1 = linea1.rstrip().split(",")
    while cta2 == menor:
        totcta += int(imp2)
        linea2 = leer(movimientos2, "max, 0")
        cta2, imp2 = linea2.rstrip().split(",")
    print("Total:", totcta)

movimientos1.close()
movimientos2.close()


"""

def leer_info(ejs, default):
    linea = ejs.readline()
    return linea if linea else default


movsbane = open("C:\mia2017\Algo1\Python\EjMergeTXT/MoviBANE.txt", 'rt')
movshb = open("C:\mia2017\Algo1\Python\EjMergeTXT/MoviHB.txt", 'rt')
movssuc = open("C:\mia2017\Algo1\Python\EjMergeTXT/MoviSUC.txt", 'rt')
max = 999999
linea = leer_info(movsbane, '999999,0')
bane_cta, bane_importe = linea.rstrip().split(',')

linea = leer_info(movshb, '999999,0')
hb_cta, hb_importe = linea.rstrip().split(',')

linea = leer_info(movssuc, '999999,0')
suc_cta, suc_importe = linea.rstrip().split(',')
total = 0

while bane_cta != max or hb_cta != max or suc_cta != max:
    tot_cta = 0
    men = min(hb_cta, bane_cta, suc_cta)  # min es una función de python
    print('cta:', men)
    while bane_cta == men:
        tot_cta += float(bane_importe)
        linea = leer_info(movsbane, '999999,0')
        bane_cta, bane_importe = linea.rstrip().split(',')
    while hb_cta == men:
        tot_cta += float(hb_importe)
        linea = leer_info(movshb, '999999,0')
        hb_cta, hb_importe = linea.rstrip().split(',')
    while suc_cta == men:
        tot_cta += float(suc_importe)
        linea = leer_info(movshb, '999999,0')
        suc_cta, suc_importe = linea.rstrip().split(',')

    print('Total por cta:', tot_cta)
    total += tot_cta
print('Total Gral:', total)

movsbane.close()
movshb.close()
movssuc.close()


"""