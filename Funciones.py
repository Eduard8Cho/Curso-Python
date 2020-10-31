import os


"""
def Mensaje():
    print('Hola mundo')

def Funcionregresa():
    return 'CADENA DE REGRESO'

def Funcion2(x):
    print('el valor de x es: ' )

def Funcionquerecibeyregresa(x,y):
    return x*y
"""

#regrresar dos o mas valores

"""
def Alumno():
    nombre='juan'              #variables locales
    edad=20                        #variables locales
    calificacion=9.5               #variables locales
    return nombre,edad,calificacion

print(Alumno()) #regresa una tupla

x,y,z=Alumno()
print(x)
print(y)
print(z)"""


os.system('cls')

def Alumno2(**kwargs): #convierte en un diccionario
    print(kwargs)
    print(kwargs['nom'])
    print(kwargs['edad'])
    print(kwargs['calif'])

def convinacion(n,*args,**kwargs):
    print(n)
    print(args)
    print(kwargs)

convinacion(10,20,30,40,nom='jaun',calif=9.5)

Alumno2(nom='juan',edad=20,calif=9.5)




"""def suma(n1,n2,n3,n4):
    return n1+n2+n3+n4

print(suma(10,10,10,10))

def suma1(n1,n2,n3,n4,n5=0): #nn=0  ese valor puede llegar o no no marca error
    return n1+n2+n3+n4+n5

print(suma1(10,10,10,10,50))"""

"""def suma2(*args): #nn=0  ese valor puede llegar o no no marca error
    print (args)
    suma=0
    for i in args:
        suma+=i

    return suma

print(suma2(10,10,10,10,50,5,3,6,9,8,7,4,5,2,1,2,2,2,5,5,2,5,5,5,5,5,2,5,2,1))


def suma3(x,*args): #nn=0  ese valor puede llegar o no no marca error
    print (args)
    suma=0
    print(x)
    for i in args:
        suma+=i

    return suma

print(suma3('este es obligatorio',10,10,10,50,5,3,6,9,8,7,4,5,2,1,2,2,2,5,5,2,5,5,5,5,5,2,5,2,1))"""


"""
Mensaje()
print(Funcionregresa())

a=5
Funcion2(a)

print(Funcionquerecibeyregresa(20,5))
"""