"""LISTAS"""


L = [2, 5, 6, 19, 3, 7]
print(L[0])
print(L[1:3])


L2 = ["A", "B"]
print(L2)


L[1:2] = L2
print(L)
print(L[-2])


L[-2] = L2
print(L)


l1 = [1, 2, 3]

"""Agregar objetos a la lista == append"""

l1.append(4)
print(l1)


"""Otra forma de hacer el append"""

l1 = l1 + [5]
print(l1)
l1.append([7, 8])
print(l1)


lista = []
for x in range(10):
    lista.append(x)
print(lista)


lista2 = list(range(10))
print(lista2)


cadena = "HOla"

"""Listar cada caracter de la cadena"""

print(list(cadena))


lista = [x for x in range(10)]
print(lista)


"""Limpiar todos los elementos de una lista."""

lista.clear()
print(lista)


lista2 = list(range(10))


"""Insertar un valor en una posición determinada."""

lista2.insert(1, 5)
print(lista2)


"""Sacar un valor de la lista, si no especificamos uno, saca el ultimo."""

lista2.pop()
print(lista2)


"""Devuelve en que posición esta el valor indicado"""

print(lista2.index(6))
l = [4, 1, 8, -3]


"""Ordenar la lista"""

print(sorted(l))
print(len(l))


l = [[4, 6], [2, 3], [1, 5]]
print(sorted(l))


x = lambda x: x * 2
print(x(5))


g = lambda x, y: x+y
print(g(5, 6))

