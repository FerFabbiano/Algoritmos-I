""" ARCHIVOS DE TEXTO """

# Un archivo es una colección de información (datos relacionados entre si), almacenados como una unidad en un
# dispositivo. No es fijo, esta limitado por el medio de almacenamiento, son dinámicos.
# Tipos: delimitados por coma (.csv (comma separated values)), sin delimitadores (.txt),
# con otro tipo de delimitadores, tabulaciones, o longitud física.
# Para abrir un archivo --> open(filename [,mode][,..]) filename --> ruta +  nombre de archivo.
# mode --> r(solo lectura), r+(lectura y escritura), w(sobreescritura), a(agrega datos), b(indica archivo binario)
# >> fh = open("c:\datos\clientes.csv","r+")
# Para leer un archivo --> .read( [tamaño]) (si se omite la cantidad, lee entero, EOF (end of file) devuelve "").
# .readline() (lee la linea completa), .readlines() (devuelve una lista de n elementos, genera tantos elementos
# como linas en el archivo).
# Para escribir un texto --> .write ("Cadena a escribir") } (si quiero que al final de la línea se grave un fin de línea
# tengo que agregar \n, de lo contrario, la cadena siguiente se grabará a continuación de esta).
# Si el archvio es r o r+ si o si debe existir. Si el archivo es w, si existe, lo pisa, sino, lo crea.
# .tell () --> Devuelve un número entero, que indica la posición a la que se está apuntando en el archivo.
# En caso de archivo binario, representa la cantidad de bytes desde el comienzo del archivo.
# .seek(posicion[,desde_donde]) --> Permite cambiar la posición a la que se apunta en el archivo. Sumará "posición",
# al parámetro "desde_donde". Este parámetro, puede tomar valor: 0(por omisión, e indica desde el principio),
# 1(desde donde se encuentra), 2(desde el final del archivo).
# .close() --> Produce el cierre del archivo, libreando los recursos pertinentes.
# with open(filename[, model]) as variable: --> Al usar la sentencia with, nos evitamos tener que cerrar el archivo
# con close, porque al finaliszar el bloque que encierra el with, el archivo es cerrado.



fzen = open("C:/Users/Fernando/Desktop/ArchivoPrueba.txt", "r+")

#texto4 = fzen.write("holahola")
#print(texto4)

# Lee la primer linea -->
#texto = fzen.readline()
#print(texto)

#texto2 = fzen.seek(0)
#print(texto2)

#texto3 = fzen.read(10)
#print(texto3)

# Imprimir linea por linea -->
#for linea in fzen:
#    print(linea)

# Devovler la cantidad de caracteres que ocupa el texto -->
#cant_caracteres = fzen.seek(0, 2)
#print(cant_caracteres)

# Para que me agregue un texto al final -->
#texto2 = fzen.seek(0, 2)
#texto2 = fzen.write("\nEsto es una pruebaaaaaaaaaaa.")
#print(texto2)

#Lee la linea indicada -->
#lineas = fzen.readlines()
#linea2 = lineas[1]
#nro, nom_ape, saldo = linea2.split(",")
#print(nro)
#print(nom_ape)
#print(saldo)


def leerArchivo(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n")
        return linea.split(",")
    else:
        return "","",""


def mostrar(nro, nom_ape, saldo):
    print("Cliente: ", nro)
    #print("Su nombre es: {0}, y su saldo es {1}".format(nom_ape, saldo))
    print(f"Su nombre es: {nom_ape}, y su saldo es: {saldo}")


#def salvar_Datos(archivo, nro, nom_ape_,saldo):
#    linea =
#    archivo.write()


fzen = open("C:/Users/Fernando/Desktop/ArchivoPrueba.txt", "r+")
fzen_nuevo = open("C:/Users/Fernando/Desktop/ArchivoPruebaNuevo.txt", "w")
nro, nom_ape, saldo = leerArchivo(fzen)
while nro:
    saldo = int(saldo) * 0.5
    mostrar(nro, nom_ape, saldo)
    nro, nom_ape, saldo = leerArchivo(fzen)
fzen.close()
fzen_nuevo.close()

