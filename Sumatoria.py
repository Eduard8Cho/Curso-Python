#suma de 1+2+3+4+...+n

import os
os.system('cls')

n=int(input('Dime hasta que numero necesitas la sumatoria: '))
i=0
suma=0
while i<=n:
    suma=suma+i
    i+=1

print('La suma es: ',suma)

os.system('cls')
suma=0
for i in range(1,n+1):
    suma=suma+i

print('La suma es: ',suma)