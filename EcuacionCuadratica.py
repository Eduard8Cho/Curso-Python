import os
import math
os.system('cls')
a=int(input('Dame el valor de a: '))
b=int(input('Dame el valor de b: '))
c=int(input('Dame el valor de c: '))

if (a!=0):

    if(b**2-4*a*c)<0:
        print('La raiz imaginaria y no se puede calcular')
    else:   
        x1=(-b+(math.sqrt(b**2-4*a*c)))/(2*a)
        x2=(-b-(math.sqrt(b**2-4*a*c)))/(2*a)
        print('x1=',x1,'\nx2=',x2)

else:
    print('Debido a que a es 0 la ecuacion no es cuadratica')

 