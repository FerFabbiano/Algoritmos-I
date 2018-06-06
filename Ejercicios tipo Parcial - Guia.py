# 1. Solicitar al usuario el ingreso de un texto. A continuación:
# a. Mostrar el texto, pero ordenado por palabra y en mayusculas
# b. Informar cuantos caracteres tiene la palabra más larga.
# c. Generar una nueva lista sin palabras repetidas.
# d. Armar un ranking de palabras, informando palabra y cantidad de ocurrencias, ordenado por
# la cantidad de ocurrencias.


def solicitarTexto (mensaje):
    texto = input(mensaje)
    return texto


def pasarTextoaLista():
    texto = solicitarTexto("Ingrese el texto con el que desea trabajar: ")
    texto = texto.upper()
    listadePalabras = texto.split()
    return listadePalabras


#print(sorted(pasarTextoaLista()))


def palabraMasLarga():
    lista = pasarTextoaLista()
    listaLargo = []
    for palabra in lista:
         listaLargo.append(len(palabra))
    return listaLargo


#print(palabraMasLarga())


def buscarPalabraMasLarga():
    lista = palabraMasLarga()
    return max(lista)


#print(buscarPalabraMasLarga())


def listaSinRepetir(lista):
    listaSinRepetir = []
    for palabra in lista:
        if palabra not in listaSinRepetir:
            listaSinRepetir.append(palabra)
    return listaSinRepetir


#print(listaSinRepetir(pasarTextoaLista()))


def armarRankingdePalabras():
    ranking = {}
    texto = solicitarTexto("Ingrese el texto a trabajar: ")
    texto = texto.split()
    for palabra in texto:
        if palabra in ranking:
            ranking[palabra] += 1
        else:
            ranking[palabra] = 1
    return ranking


ranking = armarRankingdePalabras()
rankingOrdenado = sorted(ranking.items(), key=lambda x: x[1], reverse=False)
print(rankingOrdenado)


# 5. Escribir una función que, dado un texto que se pasa por parámetro,
# lo devuelva cambiando la letra “m” por “eme”, y “M” por “EME”.


def reemplazarPalabra(texto):
        palabra_nueva = " "
        for caracter in texto:
            if caracter == "m":
                palabra_nueva += "eme"
            elif caracter == "M":
                palabra_nueva += "EME"
            else:
                palabra_nueva += caracter
        return palabra_nueva


#print(reemplazarPalabra("Hola me cago en Madre de m"))


# 7. Ingresar en un diccionario pares de datos con una clave que será el nombre de una
# ONG (Organización No Gubernamental) y el monto que será una donación. Una misma clave se puede ingresar varias
# veces. Se pide:  a. Calcular el total recaudado para cada ONG e imprimirlo sin importar un orden. b. Imprimir el
# listado anterior ordenado de mayor a menor por cantidad recaudado, indicando: cantidad – ONG


def solicitarValor(mensaje):
    valor = input(mensaje)
    return valor


def calcularTotalRecaudado ():
    recaudacion = {}
    ONG = solicitarValor("Ingrese el nombre de la ONG: ")
    donativo = int(solicitarValor("Ingrese el monto a donar: "))
    recaudacion[ONG] = donativo
    seguir = solicitarValor("Desea seguir ingresando datos? Para finalizar ingrese 0.")
    while seguir != "0":
        ONG = solicitarValor("Ingrese el nombre de la ONG: ")
        donativo = int(solicitarValor("Ingrese el monto a donar: "))
        if ONG in recaudacion:
            recaudacion[ONG] += donativo
        else:
            recaudacion[ONG] = donativo
        seguir = solicitarValor("Desea seguir ingresando datos? Para finalizar ingrese 0.")
    return recaudacion


#monto = calcularTotalRecaudado()
#montoOrdenado = sorted(monto.items(), key=lambda x: x[1], reverse=False)
#print(montoOrdenado)



# 6. Solicitar al usuario el ingreso de un texto. Considerar que el usuario solo ingresa palabras separadas por blancos,
# sin ningún otro tipo de caracteres. Mostrar una lista de las palabras capicúas ingresadas, ordenadas alfabéticamente,
# sin repetirlas. Una palabra capicúa es la que es exactamente igual al invertirla.


def solicitarTexto(mensaje):
    texto = input(mensaje)
    return texto


def armarLista():
    texto = solicitarTexto("Ingrese un texto: ")
    lista = texto.split()
    listaSinRepetir = []
    for palabra in lista:
        if palabra not in listaSinRepetir:
            listaSinRepetir.append(palabra)
    return listaSinRepetir


def palabrasCapicua():
    lista = armarLista()
    listaCapicua = []
    for palabra in lista:
        indice = 0
        indiceatras = -1
        for caracter in palabra:
            if caracter == palabra[indiceatras]:
                indice += 1
                indiceatras -= 1
        if indice == len(palabra):
            listaCapicua.append(palabra)
    return listaCapicua


#print(sorted(palabrasCapicua(), reverse=True))
