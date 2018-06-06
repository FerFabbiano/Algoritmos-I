"""Los siguiente ejercicios fueron resueltos en la clase del dia Martes 10 de Abril. Corresponden al tema de listas.
Se recomienda prestar mucha atencion a la forma de resolucion de cada uno de ellos, hasta lograr aprenderlas y comenzar
a automatizarlas. Ademas, resolver los ejercicios que quedaron sin resolver a modo de practica. Cualquier duda
u observacion es bienvenida. """

#Menu del dia Martes 10 de abril: ejercicios con listas y programacion modular.

"""Ejercicio 1: Se pide programar una funcion que, para una lista de numeros, cuente la cantidad de
elementos que sean menores a 7. Programar tambien una funcion que reemplaza en la lista todos los
elementos mayores a 6 por un 6."""


def mayoresASiete(lista):
    contador = 0
    for numero in lista:
        if numero < 7:
            contador += 1
    return contador


def mayoresASieteBis(lista):
    return len([item for item in lista if item < 7])


def remplazarporSeis(lista):
    i = 0
    while i < len(lista):
        if lista[i] > 6:
            lista[i] = 6
        i += 1


def remplazarPorSeisBis(lista):
    return [item if item < 6 else 6 for item in lista]


#lista = [1, 3, 4, 1, 3, 9, 9]


#print(remplazarporSeis(lista))
#print(remplazarPorSeisBis(lista))


"""Ejercicio 2: Se pide ingresar notas numericas en una lista hasta que el usuario decida parar.
Luego, calcular el promedio de estas"""


def SolicitarValor(mensaje):
    valor = input(mensaje)
    return valor


def IngresarNotas():
    lista = []
    seguir = True
    while seguir:
        nota = SolicitarValor("Ingrese una nota númerica, para finalizar ingrese 0.")
        if nota == "0":
            seguir = False
        else:
            lista.append(nota)
    return lista

#lista = IngresarNotas()
#print(lista)

def sumalista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma


#lista = IngresarNotas()
#print(sumalista(lista))


"""Ejercicio 3: En este caso, se nos solicita un pequeño programa.Se pide ingresar palabras en una 
lista hasta que el usuario decida parar. Luego, se pide que el programa tenga una funcion que cuente
la cantidad de palabras que contengan algun caracter que ingrese el usuario. Finalmente, imprimir 
dicho valor por pantalla"""


def solicitarValor(mensaje):
    valor = input(mensaje)
    return valor


def ingresarPalabras():
    seguir = True
    lista = []
    while seguir:
        palabra = solicitarValor("Ingrese la siguiente palabra. Para finalizar ingrese 0")
        if palabra == "0":
            seguir = False
        else:
            lista.append(palabra)
    return lista


def contarCaracterEnListaDePalabras(caracter, lista):
    contador = 0
    for palabra in lista:
        if caracter in palabra:
            contador += 1
    return contador
    #return len([item for item in lista if caracter in item])


#listaPalabras = ingresarPalabras()
#caracter = solicitarValor("Ingrese caracter")
#total = contarCaracterEnListaDePalabras(caracter, listaPalabras)
#print(total)


"""Ejercicio 4: Se pide ingresar tuplas de tres valores: el primero es el nombre de un alumno,
el segundo y el tercero son notas. Estas tuplas deben ser almacenadas en una lista hasta que el 
usuario decida frenar. Finalmente, calcular el promedio de cada alumno en una lista nueva que contenga
tuplas con dos valores (nombre, promedio) e imprimir al alumno que tenga mejor promedio con este.
Adicional: imprimir ordenadamente de mayor a menor toda la lista."""


def IngresarValor(mensaje):
    valor = input(mensaje)
    return valor


def IngresarNombre():
    seguir = True
    lista = []
    while seguir:
        nombre = solicitarValor("Ingrese nombre y apellido del alumno. Para finalizar, ingrese 0.")
        if nombre == "0":
            seguir = False
        else:
            nota1 = solicitarValor("Ingrese la nota del alumno: ")
            nota2 = solicitarValor("Ingrese la segunda nota del alumno: ")
            tupla = (nombre, nota1, nota2)
            lista.append(tupla)
    return lista


def calcularPromedio():
    lista = IngresarNombre()
    contador = 0
    listat = []
    while contador < len(lista):
        promedio = (int(lista[contador][1])/2 + int(lista[contador][2])/2)
        nombre = lista[contador][0]
        tupla = (nombre, promedio)
        listat.append(tupla)
        contador += 1
    return listat


promedioOrdenado = calcularPromedio()
print(sorted(promedioOrdenado, reverse=True))


"""Ejercicio  5: Ingresar valores en una lista. Estos valores pueden ser cadenas o numeros, pero todas
se ingresan en formato string. Programar una funcion que devuelva dos listas separadas, una con
las cadenas y otras con los elementos numericos. Estas cadenas deben ser devueltas con su orden
original invertido."""


