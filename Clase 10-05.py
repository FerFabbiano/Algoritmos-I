"""MÉTODOS DE BÚSQUEDA"""

l = [3, 5, 7 ,4 , 8, 10]

def buscar4(lista):
    return 4 in lista


#print(buscar4(l))


def buscar4Bis(lista):
    for i in lista:
        if i == 4:
            return True
    return False


#print(buscar4Bis(l))


def buscar4BisBis(lista):
    if 44 in lista:
        return True
    return False


#print(buscar4BisBis(l))


def buscarIndicePython():
    for indice, valor in enumerate(l):
        print("l[{}] = {}".format(indice,valor))


#print(buscarIndicePython())


# Mejor ordenamiento O(nlogn)


# Busqueda binaria
def busq_bin(elemento, lista):
    # Posicion del elemento, o None si no está
    ini = 0
    fin = len(lista) - 1
    while ini <= fin:
        med = (ini + fin) // 2
        if lista[med] == elemento:
            return med
        elif lista[med] > elemento:
            fin = med - 1
        else: #lista[med] < elemento
            ini = med+1
    return None


#print(busq_bin(8, l))


"""" RECURSIVIDAD """


def factorial (n):
    if n == 0: return 1
    return n * factorial(n-1)


#print(factorial(10))


# Numeros de Fibonacci
# Fib(0) = 1, Fib(1) = 1, n > 1 --> Fib(n) = Fib(n-1) + Fib(n-2)
def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)


print(fib(7))


# El algoritmo calcula bien, pero calcula muchas veces lo mismo.