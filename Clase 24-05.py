# make_translate --> "ñáÁ$" por "nnaAs" (caracter a caracter)


""" MERGE de Archivos """

# Primary key, si hay una clave única sin repetirse
# Registro centinela --> Un valor imposible, son todas las claves menores a ese numero. Me aseguro que al leer ese
# número, llegué al final.


def leer(archivo, default):  # solo me devuelve una linea de texto que voy a procesar afuera
    linea = archivo.readline()
    if linea !="":
        return linea
    else:
        return default


MAX_M = "99999, 0"
MAX_N = "99999, 0"

maestro = open("..\prueba corte de control maestro.txt", "rt")
novedades = open("..\ novedades.txt", "rt")
maestro_actual = open("..\maestro_actual.txt", "w")


lmaestro = leer(maestro, MAX_M)
lnovedades = leer(novedades, MAX_N)


while lmaestro != MAX_M or lnovedades != MAX_N:
    cta, saldo = lmaestro.rstrip("\n").split(",")
    cta_nov, imp = lnovedades.rstrip("\n").split(",")
#    while cta > cta_nov:  # Novedad no está en el maestro
#         # error("{} no existe".format(cta_nov))
#        lnovedades = leer(cta_nov, MAX_N)
#        cta_nov, imp = lnovedades.rstrip(("\n").split((",")))
    while cta == cta_nov:
        saldo += imp
        lnovedades.leer(novedades, MAX_N)
        cta_nov, imp = lnovedades.rstrip("\n").split(",")
    #  grabar (maestro_actual, cta, saldo)
    lmaestro.leer(maestro, MAX_M)


