import os
import math
os.system('cls')

"""
edad=int(input('Dame la edad de la persona: '))

condicion=edad>=18

if condicion:
    print('Ya puedes votar')
else:
    print('No puede votar')



if edad>=18:
    print('Ya puedes votar')
else:
    print('No puede votar')

if edad>=18:
    pass #no hace nada
else:
    print('No puede votar')
"""
#operadores logicos 
# and, or, not

n=int(input('Numero entre 0 y 30: ')) 

if n>=0 and n<=10:
    print('Esta e el rango del 0 al 10')
else:
    if n>10 and n<=20:
        print('Esta en el rango del 11 al 20')
    else:
        if n>20 and n<=30:
            print('Esta en el rango del 21 al 30')
        else:
            print('El numero es mayor que 30')

if n>=0 and n<=10:
    print('Esta e el rango del 0 al 10')
elif n>10 and n<=20:
    print('Esta en el rango del 11 al 20')
elif n>20 and n<=30:
    print('Esta en el rango del 21 al 30')
else: 
    print('El numero es mayor que 30')



