'''
Created on 14 oct. 2020

@author: sergiosantiago
'''

import random
maximo = 10
minimo = 0
n = -1
aleatorio = 0
def generaNumero():
    aleatorio = random.randint(minimo,maximo)
    return aleatorio

def leeNumero():
    mensaje = ("Escriba un numero entre {} y {} ").format(minimo, maximo)
    n = int(input(mensaje))
    return n

def comprobar():
    if aleatorio == n:
        print("Has acertado")
        return True
    else:
        if (n > aleatorio):
            print("El numero es menor")
        else:
            print("El numero es mayor")

if __name__ == "__main__":
    aleatorio = generaNumero()
    while (n != aleatorio):
        n = leeNumero()
        comprobar()