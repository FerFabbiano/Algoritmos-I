#Ejercicio 1: Se pide un programa que registre el resultado de una votación. Para esto, se le debe pedir a un usuario
# que ingrese votos (únicamente el nombre del partido politico) hasta que decida finalizar. Una vez que finalice, se
# debe imprimir ordenadamente (de mayor a menor) el resultado de la votación (es decir, cada partido político con su
# cantidad de votos correspondiente.


def solicitarVoto(mensaje):
    valor = input(mensaje)
    return valor

def contarVotos():
    seguir = True
    padron = {}
    while seguir:
        partido = solicitarVoto("Ingrese el nombre del partido politico votado. Para finaliza ingrese 0.")
        if partido != "0":
            if partido in padron:
                padron[partido] += 1
            else:
                padron[partido] = 1
        else:
             seguir = False
    return padron


#d = contarVotos()
#padron_ordenado = sorted(d.items(), key=lambda x: x[1], reverse=True)
#print(padron_ordenado)


# Ejercicio 2: Se pide un programa que analice promedios de alumnos universitarios. Para esto, se debe pedir al usuario
# que ingrese un alumno con 3 notas hasta que este decida finalizar. Una vez que termina, se debe obtener el promedio de
# cada uno de ellos, para finalmente imprimir a por pantalla los 3 alumnos cuyo promedio sea el más alto.


def SolicitarValor(mensaje):
    valor = input(mensaje)
    return valor


def armarLista ():
    seguir = True
    listaAlumnos = {}
    while seguir:
        alumno = SolicitarValor("Ingrese el nombre del alumno. Para finalizar ingrese 0.")
        if alumno != "0":
                listaAlumnos[alumno] = int(SolicitarValor("Ingrese una nota numerica: ")) / 3 + \
                                       int(SolicitarValor("Ingrese una nota numerica: ")) / 3 + \
                                       int(SolicitarValor("Ingrese una nota numerica: ")) / 3
        else:
            return listaAlumnos


lista = armarLista()
mejorPromedio = sorted(lista.items(), key=lambda x: x[1], reverse=True)
print(mejorPromedio)
