#adivine un numero a la computadora
#que numero estoy pensando 

import random
import os

os.system('cls')

num=random.randint(1,10)
n=0
i=1
while i<=3:
    n=int(input('Intenta adivinar: '))
    if n==num:
        print('¡GENIAL LO HICISTE!')
        break
    elif n<num:
        print('No, mas grande')
    else:
         print('No, mas pequeño')
    i=i+1

if i!=3:
    print('El numero en el que pense es: ',num)
