# Ejercicio 1: Excribir una funcion que se pasa por parametro, lo imprima al reves y sin ninguna vocal.
# las vocales pueden estar en minusculas o mayusculas.


def darVueltaelTexto (texto):
    textoalReves = texto[::-1]
    return textoalReves


def sacarVocales(texto):
    texto = texto.lower()
    texto_Nuevo = ""
    listaMinusculas = ["a", "e", "i", "o", "u"]
    for caracter in texto:
        if caracter not in listaMinusculas:
            texto_Nuevo += caracter
    return texto_Nuevo


#textoFinal = sacarVocales(darVueltaelTexto("HolA que tal"))
#print(textoFinal)


# Ejercicio 3: Ingresar en un diccionario pares de datos con una clave que será un nombre de Partido Politico y valor
# que será la cantidad de votos obtenidos en una provincia, una misma clave puede ingresar varias veces. Se pide:
# a) Calcular el total de votos para cada partido e imprimirlo
# b) Imprimir el listado anterior ordenado de mayor a menor por cantidad de votos.


def solicitarValor(mensaje):
    valor = input(mensaje)
    return valor


def contarVotos():
    padron = {}
    partidoPolitico = solicitarValor("Ingrese el nombre del Partido Politico: ")
    padron[partidoPolitico] = 1
    seguir = solicitarValor("Desea seguir ingresando datos? Para finalizar ingrese 0.")
    while seguir != "0":
        partidoPolitico = solicitarValor("Ingrese el nombre del Partido Politico: ")
        if partidoPolitico in padron:
            padron[partidoPolitico] += 1
        else:
            padron[partidoPolitico] = 1
        seguir = solicitarValor("Desea seguir ingresando datos? Para finalizar ingrese 0.")
    return padron


#print(contarVotos())


# Ejercicio 2: Solicite al usuario el ingreso de un texto. El mismo debe contener al menos 100 palabras, de lo contrario
# deberá exigir al usuario que ingrese más palabras, y adicionarlas a las ya ingresadas hasta superar el mínimo
# establecido. Considere que el usuario solo ingresa palabras separadas por blancos, sin ningun otro tipo de caracteres.
# Muestre una lista de palabras ingresadas, ordenada alfabeticamente, sin repetir palabras.


def ingresarTexto(mensaje):
    texto = input(mensaje)
    return texto


def crearListadePalabras():
    texto = solicitarValor("Ingrese texto a trabajar: ")
    listadePalabras = texto.split()
    while len(listadePalabras) < 4:
        texto = solicitarValor("Falta agregar palabras: ")
        listadePalabras += texto.split()
    return listadePalabras


def eliminarRepetidas(lista):
    listasinRepetidas = []
    for palabra in lista:
        if palabra not in listasinRepetidas:
            listasinRepetidas.append(palabra)
    return listasinRepetidas


listaOrdenada = sorted(crearListadePalabras(), reverse=False)
listaSinRepetidas = eliminarRepetidas(listaOrdenada)
print(listaSinRepetidas)

