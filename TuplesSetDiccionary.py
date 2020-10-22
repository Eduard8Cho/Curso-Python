import os

os.system('cls')
"""
#las tuplas no se pueden modificar
t=(1,2,3,4,5)
print(t[1:4]) #recordar que le 4 no lo toca

for i in t:
    print(i)

l=list(t)
print(type (l))
print(type (t))
t2=tuple(l)
print(type (t2))

#para borrar algun 
del l[2]
#para agregar
l.pop()
l.remove()
"""

#conjuntos (SET)

Programacion={'juan','pedro','maria','diana'} 
calculo={'jesus','eduardo','gonzalo','santiago','santiago'} #aunque se repitan no lo imprime si son los mismos
"""
print(Programacion)
print(calculo)
#print(Programacion[0]) los conjuntos no tiene posiciones por ende no se puede hacer esto
# ademas no las imprime en orden 
print('maria'in Programacion)

#para agregar 
Programacion.add('eduardo')

#para sacar del conjunto

Programacion.remove('maria')
print(Programacion)

del Programacion
print(Programacion)
"""
"""
#juntar unir

C2=Programacion | calculo
print(C2)

#resta
C2=Programacion-calculo
print(C2)
"""
"""
#Diccionarios (JSON)

alumnos={'nombre':'juan','edad':'20 años','carrera':'ingenieria en computacion'}
print(alumnos)
alumnos={'nombre':'juan',
            'edad':'20 años',
            'carrera':'ingenieria en computacion'}

print(len(alumnos)) #len perimite saber cuantos elementos tiene
#print(alumnos[0]) no podemos axesar ´por posicionpero si por 

print(alumnos['nombre'])
print(alumnos.get('edad'))

# para agregar si no existe lo agrega y si ya existe solo lo modifica

alumnos['promedio']=9.5
print(alumnos)
print(len(alumnos))

#como imprimir un diccionario

for i in alumnos:
    print(i)      #imprime los key

for i in alumnos:
    print(alumnos[i])

print(alumnos.values())  #los valores
print(alumnos.keys())   #los keys
print(alumnos.items())  #una lista de tuplas 

#para manejarlos por separado 


for j,i in alumnos.items():
    print(j)
    print(i)
"""
alumnos1={'nombre':'juan',
            'edad':'20 años',
            'carrera':'ingenieria en computacion'}
alumnos2={'nombre':'eduardo',
            'edad':'20 años',
            'carrera':'ingenieria en mecatronica'}

alumnos=[alumnos1,alumnos2]

for a in alumnos:
    print((a['nombre'],a['edad'],a['carrera']))
