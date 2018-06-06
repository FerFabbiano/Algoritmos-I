"""Ejercicio: determinar la cantidad de veces que se encuentra la letra h"""


def encontrarLetra(texto, letra):
    texto = texto.lower()
    """Asi, me aseguro de que si hay alguna letra mayuscula, me la cuente igual"""
    cont = 0
    for caracter in texto:
        if caracter == letra:
            cont += 1
    return cont


#print("Cantidad de letras: ", encontrarLetra("Hola", "h"))


"""Ejercicio: Eliminar las letras h de un texto (las cadenas de caracteres son inmutables, puede generar otro texto)"""


def eliminarLetra(palabra, letra):
    palabra_nueva = ""
    for caracter in palabra:
        if caracter != letra:
            palabra_nueva += caracter
    return palabra_nueva


#print(eliminarLetra("Holahhhh", "h"))


"""Ejercicio: ver si la secuencia esta ordenada"""


def secuenciaOrdenada(texto):
    indice = 0
    while indice < (len(texto)-1):
        if texto[indice] > texto[indice+1]:
            return False
        else:
            indice += 1
    return True


#print(secuenciaOrdenada("1234"))


"""TAREA 05/04/2018"""


"""Ejercicio: Dado un texto, determinar si es capicua"""


def capicua(palabra):
    indice = 0
    indiceatras= - 1
    for caracter in palabra:
        if caracter == palabra[indiceatras]:
            indice += 1
            indiceatras -= 1
    if indice == len(palabra):
        return True
    else:
        return False


#print(capicua("neuquenm"))


"""Ejercicio: Dados dos textos, determinar si el segundo es un prefijo del primero"""


def prefijo(palabra_1, palabra_2):
    pref = palabra_1[:len(palabra_2)]
    if pref == palabra_2:
        return True
    else:
        return False


#print(prefijo("inutil", "in"))


"""Ejericio: Dado una cadena de caracteres reemplazar una con otra teniendo en cuenta lo siguiente: a-c b-d z-b, 
RECORDAR: Las cadenas de caracteres son inmutables, debo crear una nueva palabra"""


def reemplazarLetra(palabra):
    palabra_nueva = " "
    for caracter in palabra:
        palabra_nueva += chr(ord(caracter)+2)
    print(palabra_nueva)


print(reemplazarLetra("Hola que tal"))
