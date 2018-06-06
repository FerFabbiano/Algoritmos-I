'''

Vamos a ver pilas y colas -> un poco de objetos

Pilas: El último elemento que entra es el primero que sale (UEPS (Último en entrar, primero en salir) -> Sistemas LIFO)
Colas: (PEPS (primero en entrar primero en salir) -> Sistemas FIFO

PILAS:

Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> pila = [5,32,4,8,10,1,12]
>>> pila
[5, 32, 4, 8, 10, 1, 12]
>>> pila.append(2)
>>> pila
[5, 32, 4, 8, 10, 1, 12, 2]
>>> pila.append(6)
>>> pila
[5, 32, 4, 8, 10, 1, 12, 2, 6]
>>> proximo = pila.pop()
>>> proximo
6
>>> pila
[5, 32, 4, 8, 10, 1, 12, 2]
>>>

----------------------------------------------
Pilas (Stack)
Realice un programa que "simule" el Stack Pointer (registro que mantiene la posicion actual de la pila de llamadas de una CPU)
Considerelo simplemente como un valor inicializado en SP = 255 que se decrementa cada vez que se añade un elemento
Al stack (pila) y se incrementa cuando se libera un elemento. De modo que si la cola esta vacia, SP = 255, si tiene 5 elementos SP = 250, etc...
Teniendo en cuenta la variable SP, utilice la pila como una forma de almacenar el valor actual de una variable
(apilando = PUSH) y luego recuperarlo (desapilando = POP) cuando se requiera usar aquel valor ya modificado por una funcion modificar(valor)
Considere la implementacion de un diccionario con claves "pila" y "SP"
{'pila' = []: 'SP' = 255} =>(si le paso 'a,b,c') {'pila' = ['a,b,c']: 'SP' = 254}


'''

def apilar(valor, dic):
    dic['pila'].append(valor)
    dic['sp'] -= 1
    return dic

def desapilar(dic):
    dic['sp'] += 1
    return dic['pila'].pop()

dic = {
    'pila' : [1,2,3,4],
    'sp' : 255
}

apilar(8,dic)
#print(dic)

'''
((5*4)+2)/11 -> 5 4 * 2 + 11 / (Notación Polaca Inversa)

'''

'''

COLAS:

Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from collections import deque
>>> cola = deque([15,2,8,4])
>>> cola
deque([15, 2, 8, 4])
>>> cola.append(4)
>>> cola
deque([15, 2, 8, 4, 4])
>>> print(cola.pop())
4
>>> print(cola.popleft())
15
>>> cola
deque([2, 8, 4])
>>>

----------------------------------------------
QUEUE (colas)
Considere la cola para entrar al campo de un recital. Hay campo general y campo vip mezclados en la misma cola.
La cola avanza normalmente una vez que han ingresado primero todas las personas con campo vip en el mismo orden que estaban en la cola principal.
Considere un diccionario con claves unicas en donde la clave indica el numero en la cola y el valor de la clave indica "vip" o "general".
Imprima en pantalla el orden en que ingresan al estadio y desacole la nueva cola.

diccionario = {1: "VIP", 2: "GENERAL", 3: "VIP", }

HACER EJERCICIO DE PAGAR BOLETAS EN RAPIPAGO:
[{"ANA": 3}, {"JUAN": 58}, {"PEPE": 8}]
TENIENDO EN CUENTA QUE EL RAPIPAGO DEJA ABONAR COMO MAXIMO 10 BOLETAS, EN CASO DE TENER MAS LE HACE HACER LA COLA DE NUEVO

'''

from collections import deque

cola = deque([1, 2, 5, 8])
print(cola)
