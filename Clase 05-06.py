""" POO --> Programación orientada a objetos """

"""

Java --> lenguaje especificamente orientado a objetos.
objeto --> es una entidad que puede recibir mensajes, responder a los mismos y enviar mensajes a otro objetos.
mensaje --> es la interacción entre quien pide un servicio y el objeto que lo brinda.
comportamiento --> las posibles resuestas a los mensajes recibidos por un objeto.
clase --> es el tipo de un objeto. Una clase agrupa a todos los objetos que tienen el mismo comportamiento.
estado del objeto --> son las propiedades que posee. A estas propiedades se las llama atributos. 
médtodos del objeto --> es la implementación de la respuesta de un objeto a los mensajes que debe recibir. Son similares
a las funciones en la programación estructurada.
Un objeto puede ser atributo de otro objeto.

"""

class curso:
    # atributos
    nombre = ""
    alumnos = {}
    # métodos
    def ponerNombre(self, nombre):
        self.nombre = nombre
    def verNombre(self):
        return self.nombre
    def agregarAlumnoYNota(self, alumno, nota):
        self.alumnos[alumno] = nota
    def cantidadAlumnos(self):
        return len(self.alumnos.keys())
    def notaAlumno(self, alumno):
        return self.alumnos[alumno]
    def alumnoEnCurso(self, alumno):
        return alumno in self.alumnos


curso1 = curso()
curso1.ponerNombre("Acero")
#print(curso1.verNombre())
curso1.agregarAlumnoYNota("Uriel", 4)
curso1.agregarAlumnoYNota("Santiago", -5)
curso1.agregarAlumnoYNota("Ezequiel", 10)

#if curso1.alumnoEnCurso("Ezequiel"): print("Esta")
#if not curso1.alumnoEnCurso("Guarna"): print("No esta")

notaSantiago = curso1.notaAlumno("Santiago")
#print(notaSantiago)


# Ejercicio --> Pila
# requerimientos : apilar, desapilar, ver la cantidad de elementos, ver el tope, preguntar si la pila esta vacía


class pila:
    # atributos
    pila = []
    # métodos
    def crearPila(self, lista):
        self.pila = lista
    def apilar(self, valor):
        self.pila.append(valor)
        return self.pila
    def desapilar(self):
        self.pila.pop()
        return self.pila
    def cantElementos(self):
       return len(self.pila)
    def verTope(self):
        return self.pila[-1]
    def pilaVacia(self):
        if len(self.pila) == 0:
            return True
        else:
            return False
    def verPila(self):
        return self.pila


pila1 = pila()
pila1.crearPila([1, 8, 5])
#print(pila1.apilar(2))
#print(pila1.desapilar())
#print(pila1.cantElementos())
#print(pila1.verTope())
#print(pila1.pilaVacia())
#print(pila1.verPila())

# LOS MÉTODOS SIEMPRE VAN CON PARÉNTESIS, LOS ATRIBUTOS NO.
# EL OBJETO SIEMPRE TIENE QUE ESTAR ASOCIADO A UN MÉTODO O ATRIBUTO.

# Ejercicio --> Cola
# requerimientos --> encolar, esta vacia, desencolar, ver próximo, cantidad de la cola

from collections import deque
class cola:
    # atributos
    elementos = []
    # métodos
    def crearCola(self, lista):
        self.elementos = lista
    def encolar(self, valor):
        self.elementos.append(valor)
        return self.elementos
    def desencolar(self):
        self.elementos.pop()
        return self.elementos
    def colaVacia(self):
        if self.elementos == 0:
            return True
        else:
            return False
#    def verPróximo(self):

    def cantElementos(self):
        return len(self.elementos)

cola1 = cola ()
cola1.crearCola([2, 4, 5])
print(cola1.encolar(2))
print(cola1.desencolar())
print(cola1.colaVacia())
print(cola1.cantElementos())