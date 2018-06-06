""" MANEJO DE ERRORES """

# Se hace a través de exepciones.


"""

def inversa():
    temp = None
    while temp == None:
        try:
            temp = int(input("Ingrese la temperatura: "))
        except ValueError: # Si hay un value error, hace lo siguiente:
            print("El valor ingresado no es valido")
    print("La inversa de T es {}".format(1/temp))


#        raise ValueError # Manda el error de vuelta
#    except ZeroDivisionError:
#        print("No se puede dividir por cero")
#    except: #El programa nunca va a explotar
#        print(("No se que paso"))
#    else: #Si no entra en ningun except
#        print("Else")
#    finally: # Sin importar lo que pase, ejecuta el finally
#        print("Finalmente!!!")

try:
    inversa()
except ValueError:
    print("Value Error en inversa().")
except ZeroDivisionError:
    print("Division por cero")

"""

# Code 0, quiere decir que ejecuto el código normalmente. No hubo ningún error.
# Process finished with exit code 1, el programa no se completó correctamente.
# base 10 --> uso 10 como base. Digitos del 0 al 9.
# base 2 --> uso 0 y 1. 1010 en base 2 es 10 en base decimal.
# base 16 --> Digitos del 0 al 9, simbolos de a - f.
# cambio de base --> temp = int(input("Ingrese la temperatura: "), 16))


""" ARCHIVOS BINARIOS """


import pickle
# Pickle nos va a permitir guardar estrucuturas y variables de Python en un archivo binario
with open("ejemplo.pkl", "wb") as archivo:
    pkl = pickle.Pickler(archivo)
    lista = [1, 3, 5, 7, 10]
    lista2 = [3, 40, 100]
    diccionario = {"color": "rojo", "temp": 15}

    pkl.dump(lista)
    pkl.dump(lista2)
    pkl.dump(diccionario)



# Una vez que guarde los elementos, no puedo reemplazar o borrar elementos.

