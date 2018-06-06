import pickle

"""

with open("ejemplo.pkl", "rb") as archivo:
    data = pickle.load(archivo) # El load recupera un elemento del archivo
    print(data)
    data = pickle.load(archivo)  # El load recupera un elemento del archivo
    print(data)
    data = pickle.load(archivo)  # El load recupera un elemento del archivo
    print(data)

"""

with open("ejemplo.pkl", "rb") as archivo:
    seguir = True
    while seguir:
        try:
            data = pickle.load(archivo) # El load recupera un elemento del archivo
        except EOFError:
            seguir= False
        else:
            print(data)

# EOF "End of file error"


def leer_desde_archivo(pfl_file):
    """ Lee del archivo pkl_file un elemento. pkl_file tiene que estar abierto en modo binario y de lectura (rb). """
    try:
        data = pickle.load(pkl_file)  # El load recupera un elemento del archivo
        fin_de_archivo = False
    except EOFError:
        data = None
        fin_de_archivo = True
    return  data, fin_de_archivo


def guardar_en_archivo(pkl_file, contenido):
    """ Guarda lo que le pasan como segundo parámetro en el archivo pkl_file. pkl_file tiene que estar abierto en modo
    escritura y binario (wb). """
    pickler = pkl.Pickler(pkl_file)
    pickler.dump(contenido) # .dump guarda






