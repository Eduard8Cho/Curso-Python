

#Listas unidimencionales
#Listas bidimencionales 
#listas tridimencionales 
#lisyas Multidimencionales 
"""
x=[1,2,3,4,5]
nombres=[1,2,True,7,[1,'Eduardo'],20,'Aldo','Eduardo']
m=[[1,2,3],[4,5,6],[7,8,9]]
print(m)
print(m[1][1])
print(nombres[4][1])




print(nombres[4])
print(nombres[-1]) #trae desde atras el valor es decir Eduardo
print(x)
#print(type(x))
print(len(nombres)) #numero de elementos de la lista 

print(nombres[1:5]) #inlcuyente:no incluyente

print(nombres[0:5]) #son lo mismo 
print(nombres[:5]) 


print(nombres[4:]) #todo a partir del 4

print(nombres[0::2]) #el 2 es e incremento
print(nombres[0::3]) #el 3 es e incremento
print(nombres[::3]) #el 3 es e incremento

print(nombres[::]) #Trae todo
print(nombres[::-1]) #Trae todo al reves
print(nombres[-1:-5:-1]) #Trae todo al reves
"""
#listas: (mutables, indices)
#tuplas (inmutables,indices)
#conjuntos: (no indices)
#diccionarios 
nombres=[1,2,True,7,[1,'Eduardo'],20,'Aldo','Eduardo']
nombres=[]
nombres.append('juan') #append sirve para agregar elementos
nombres.extend([1,2,3]) #agregar otra lista al final de la lista 
nombres.pop(3) #elimina un valor de la lista 
nombres[1]=('Temporal') #Asignar un nuevo valor
print(nombres)

noms=('juan','maria') #una tupla es entre parentesis 
print(noms[::]) #en esta no se pueden agregar mas cosas es decir no hay append (todo lo anterior aplica [::])
