import os
os.system('cls')
"""
lista=[[1,2,3],[4,5,6],[7,8,9]]
#print(lista)

for i in lista:
    for j in i:
        print(j,end=' ')
    print()
#para impirmir con formato

lista=[[1,2,3,4,5],[4,56,64],[7,'juan',9]]
#print(lista)

for i in lista:
    for j in i:
        #< justifica a la izquierda
        #>justifica a la derecha 
        print("{0:<5}".format(j),end=' ')
        #el 5 es el espacio de separado
    print()

"""

#llenando del teclado

lista=[]

r=int(input('Cuantos renglones quieres:'))
c=int(input('Cuantas columnas quieres:'))

for i in range(0,r):
    lista.append([])    
    for j in range(0,c):
        lista[i].append(int(input('Digita lo que quieres poner en la lista:')))
for i in lista:
    for j in i:
        print("{0:<5}".format(j),end=' ')
    print()