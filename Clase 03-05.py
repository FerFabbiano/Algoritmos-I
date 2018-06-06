# variable atomica --> un único dato
# estructuradas --> lista, tupla, etc.
# ordenar --> debo tener un criterio de ordenameinto, sino no puedo ordenar
# cuando busco algo, si esta ordenado, me voy a ver beneficiado


""" ALGORITMOS DE ORDENAMIENTO """
# Ordenamiento burbuja / por burbujeo (bubble sort)
# Solo para listas (tuplas no porque son inmutables)


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


""" Complejidad algoritmica """
# temporal
# espacial (cuando memomoria va a ocupar)
# si tengo un solo for --> orden lineal
# si tengo dos for --> orden cuadratico
# O(1) --> constante
# O(n) --> depende de n, no es constante


""" ALGORITMOS DE ORDENAMIENTO """

# Ordenamiento por selección / Selection Sort

l = [1, 2, 3, 10, 4, 5]

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_indice = i
        for j in range(i+1, len(arr)):
            if arr[min_indice] > arr[j]:
                min_indice = j
        arr[i], arr[min_indice] = arr[min_indice], arr[i]
    return arr


print(selectionSort(l))


# Ordenamiento mejorado, si esta ordenado, sale del for


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        cont = 0
        for j in range(n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cont += 1
        if cont == 0:
            break
    return arr


print(bubbleSort(l))


# Ordenamiento por inserción (Insertion Sort)


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        k = arr[i]
        j = i - 1
        while j > 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
    return arr


print(insertionSort(l))