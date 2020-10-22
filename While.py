"""
solo existen dos ciclos en python 
while
for

n=n+1
n+=1

"""




import os
import math

os.system('cls')

"""
n=0
while n<=5:
    print(n,'Mensaje')
    n=n+1

range (donde_empieza, hasta_donde, de_cuanto_en_cuanto)

for n in range(2,10,2):
    print(n,'Mensaje')
"""
resp='si'

while resp =='si' or resp=='Si'or resp =='SI' or resp=='sI':
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
    resp=input('Desea ejecutar otra vez el programa: ')