"""Tema de hoy: diccionarios"""


d = {"clave1": 4, "clave2": 2}


"""Puedo tener claves distintas, con vlores iguales. No puedo tener iguales claves con valores distintos."""


#if "clave1" in d:
#    print("Esta")
#else:
#    print("No esta")


#if 1 in d.values():
#    print("Esta")
#else:
#    print("No esta")


"""El primero me busca la clave, el segundo me busca el valor en el diccionario.
A partir de claves puedo acceder a valores, pero a partir de valores no puede acceder a claves."""


valor2 = d["clave2"]
valor3 = d.get("clave3", [1, 2, 3])

#print(valor2, ",", valor3)


claves = d.keys()
#print(claves)


valores = d.values()
#print(valores)


claves_y_valores = d.items()
#print(claves_y_valores)


futbolistas = {
    "messi": 607,
    "CR7": 651,
    "pele": 767,
    "Muller": 735,
    "Bican": 805
}


#print(futbolistas)


#for clave in futbolistas:
    #itera las claves
#    print(clave, futbolistas[clave])


#for futbolista in futbolistas.keys():
#    print(futbolista, futbolistas[futbolista])


for goles in futbolistas.values():
    print(goles)


#for futbolista, goles in futbolistas.items():
#    print(futbolista, goles)


#sorted devuelve lista

#futbolistas_ordenados = sorted(futbolistas)
#print(futbolistas_ordenados), type(futbolistas_ordenados)

#reverse me ordena de mayor a menor

#goles_ordenados = sorted(futbolistas.values(), reverse=True)
#print(goles_ordenados)


#futbolistas_ordenados_por_goles = sorted(futbolistas.items(), key=lambda x: x[1], reverse=False)
#x[1] va a buscar el valor de la clave, que esta en la posición 1, en la 0 esta la clave
#print(futbolistas_ordenados_por_goles)


"""Uno de los usos mas comunes para un diccionario es la de funcionar como acumulador ya que nos permite fácilmente
reasginar valores para un clave que este en el diccionario. Un ejemplo de este uso podria ser el de contar la cantidad
de veces que aparecen distintos caracteres en un texto."""


#Ejercicio
def frecuencias(texto):
    diccfrecuencias = {}
    for caracter in texto:
        if caracter != "":
            if caracter in diccfrecuencias:
              diccfrecuencias[caracter] += 1
            else:
                diccfrecuencias[caracter] = 1
    return diccfrecuencias


texto = "Hola como estas"
diccfrecuencias = frecuencias(texto)
print(diccfrecuencias)
frecordenado = sorted(diccfrecuencias.items(), key=lambda x: x[1], reverse=True)
print(frecordenado)




