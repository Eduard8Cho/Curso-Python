#Programa que sume las calificaciones y me de el promedio y imprimir la calificacion mas alta 

import os
os.system('cls')
n_calificaciones=int(input('Dime cuantas calificaciones vas a ingresar: '))

i=0
s=0
m=0
for i in range(1,n_calificaciones+1):
     calificacion=int(input('Dame la calificacion: '))
     if calificacion>m:
         m=calificacion
     s=s+calificacion

prom=s/n_calificaciones
print('El promedio es: %.2f\nY la calificacion mas alta es: %d'%(prom,m))