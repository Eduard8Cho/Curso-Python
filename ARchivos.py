#bianiros (imagenes, audios etc)
#atexto (texto)

#4 maneras de abri r,a,w,x      read,append,escribir,crear
"""f=open('alumnos.txt','w' ) #abrir archivos w es el modo de apertura + concatena pero de debe convertir i a cadena 
for i in range(5):
    f.write('Cadena '+str(i)+'\n')
f.close()"""


"""f=open('alumnos.txt','r')
print(f.read()) #imprime too lo que hat en el archivo y esto lo puedo guaradar en una variable 
datos=f.read()
#print (datos)
print(type(datos))

#datos=f.read(5) #el numero 5 lee solo los primeros 5 caracteres de la cadena (archivo de texto)
print(datos) #//puede recivir valores o no

datos#=f.readline() #trae solo un renglos si se pone dos veces la funcion imprime renglon por renglon
datos=f.readlines() #trae la informacion en una lista y no en una cadena 

for i in datos:
    #print( i[:-1] )
    print(i,end="")

f.close()"""

datos=None # se declara una variable



try:
    f=open('alumnos.txt','r')
    #datos=f.read(5)
    #datos=f.readline()
    datos=f.readlines()
    print(datos)
    f.close()
except IOError as e:
    print('Error al abrir el archivo---',e.errno)


if datos!=None:
    for i in datos:
        #print(i[:-1])
        print(i,end="")





