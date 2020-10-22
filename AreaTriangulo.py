import os
import math

os.system('cls')

a=int(input('Digita el lado a: '))
b=int(input('Digita el lado b: '))
c=int(input('Digita el lado c: '))

#Operadores Aritmeticos: " +,-,*,/,//,%(reciduo),**(potencia) "
#Operadores Relacionales: " >,<,<=,>=,==,!= "
#Operadores Logicos: "and,or,not"
#Operadores Especiales:

s=(a+b+c)/2

A=math.sqrt(s*(s-a)*(s-b)*(s-c))

print('El area es: ',A) #con muchos decimales 
print('El area es: %.2f'%A) #con el numero de decimales indicados (solo una forma hay muchas mas)
print('El triangulo de lado %d,%d,%d tiene un area de: %.2f'%(a,b,c,A)) #inprimir varias variablels al mismo tiempo

print(7//3) #solo el entero de la divicion 
print(7%3)  #reciduo
print(2**8) #potencia
print(math.pow(2,8))  #potencia con punto decimal 

