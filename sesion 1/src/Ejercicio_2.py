'''
Created on 14 oct. 2020

@author: sergiosantiago

'''
import random

objetivo = random.randint(1,10)
maximo = 10
minimo = 1
mensaje = ("Introduzca un numero desde el minimo: {} hasta el maximo: {} ").format(minimo, maximo)

a = int(input(mensaje))
print("El numero introducido es",a)
if (a == objetivo):
    print("Has acertado")
else:
    print("Has fallado, el numero era:", objetivo)