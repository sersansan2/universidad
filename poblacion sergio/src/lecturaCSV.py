#!/usr/local/bin/python3
import csv
import matplotlib.pyplot as plt

rutaArchivo = "/Users/sergiosantiago/Downloads/Poblacion/data/population.csv"

class datosPaises():
    nombre = ""
    codigo = ""
    year = 0
    poblacion = 0
    
    def __init__(self, nombre: str, codigo:str, year:str, poblacion:str):
        self.nombre = nombre
        self.codigo = codigo
        self.year = int(year)
        self.poblacion = int(poblacion)

def leerCSV(name: str):
    with open(name, mode='r') as f:
        file = csv.reader(f)
        datosPaisesLista = []
        for i in file:
            datosPaisesLista.append(datosPaises(i[0], i[1], i[2], i[3]))
        print(len(datosPaisesLista))
        return datosPaisesLista
            
def calcularDatos(lista:list):
    paises = set()
    for i in lista:
        paises.add(i.nombre)
        
    print("Hay {} países en el csv".format(len(paises)))
    return paises

def compararPoblaciones(lista: list, conj: set, year: int):
    solicitud = year - 1960
    for i in range(1, len(conj)):
        print(lista[i * solicitud].nombre, "y su poblacion es:", lista[i * solicitud].poblacion )
        print(i * solicitud)

def obtenerPoblacionesPais(nombre:str, lista: list):
    band = False
    poblaciones = [[],[]]
    for i in lista:
        if i.nombre == nombre:
            poblaciones[0].append(i.year)
            poblaciones[1].append(i.poblacion)
            band = True
        elif band == True and i.nombre != nombre:
            break
    plt.title('Historial de población')
    plt.plot(poblaciones[0],poblaciones[1])
    plt.ylim(poblaciones[1][0],poblaciones[1][-1])
    plt.xlabel("Años")
    plt.ylabel("Población")
    plt.show()
    return poblaciones
    
obtenerPoblacionesPais("Small states", leerCSV(rutaArchivo))
compararPoblaciones(leerCSV(rutaArchivo),calcularDatos(leerCSV(rutaArchivo)),2016)