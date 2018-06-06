"""Si lo que voy a agregar es un elemento suelto, uso append, si lo que le voy a agregar es otra lista, uso extend."""


"""Ejemplo: l1 representa p(x)=3+x-2x^2+5x^3. l2 representa p(x)=2+0x+x^2+x^3. 
Hacer una funcion que le paso p1 y p2, y devuelve la suma."""


def sumarpolinomios(lista1, lista2):
    indice2 = 0
    lista3 = []
    if len(lista1) == len(lista2):
        for numero in lista1:
            numero += lista2[indice2]
            lista3.append(numero)
            indice2 += 1
    return lista3


lista1 = [3, 1, -2, 5]
lista2 = [2, 0, 1, -1]
#print(sumarpolinomios(lista1, lista2))


def sumapolinomio(p1, p2):
    lista = []
    while len(p1 != len(p2)):
        print(len(p2))
        if len(p1) > len(p2):
            p2.append(0)
        else:
            p1.append(0)
    for i in range(len(p1)):
        lista.append(p1[i] + p2[i])
    return lista


"""No imprimo ni cargo las listas dentro de la función."""
p1 = [3, 1, -2, 5]
p2 = [2, 0]
print(sumarpolinomios(p1, p2))


def f2(l):
    l.append(8)


l = [4, 3, 2]
f2(l)


#print(l)


"""Ejercicio: Definir una función a la que se le pasa una lista de enteros y un número, devuelve la posición en la que
está el número o -1 si no la encuentra. Sin usar in ni count."""


def verificarPosición(lista, numero):
    cantidad = len(lista)
    for i in range(cantidad):
        if lista[i] == numero:
            return i
    return -1


print(verificarPosición([1, 2, 3], 1))


"""algoandres@yahoo.com"""