import os
import leer

from leer import leerpromedio,leeredad,leerentero



os.system('cls')


menu="""
    MENU (CRUD)
    1. Altas (C)
    2. Bajas (D)
    3. Consultas (R)
    4. Actualizar (U)
    5. Reportes (R)
    6. Salir
    """
opc=None
alumnos=[]


def buscar (alumnos,cuenta):
    existe=False
    indice=-1
    for  a in alumnos:
        indice += 1
        if a['Numero_de_Cuenta']==cuenta:
            existe=True
            break
    return existe,indice

def Buscar_Archivos(alumnos,Id):
    existe=False
    indice=-1
    for d in alumnos:
        a=d.split(',')
        indice+=1
        if int(a[0])==Id:
            existe=True
            break
    return existe,indice



while opc!=6:
    print(menu)
    opc=leer.leerentero('Digita una Opcion')

 

    if opc==1:
        try:
            f=open('DOCALUMNOS.txt','r')           
            n=f.readlines()
            f.close()                                            
        except IOError as e:
            print('Error al abrir el archivo -- ',e.errno)

        try:
            f=open('DOCALUMNOS.txt','a')
            Numero_de_Cuenta=int(len(n)+1)
            Nombre=(input('Nombre:')) 
            Edad=leer.leeredad('Edad:') 
            Carrera=(input('Carrera:'))
            Promedio=leerpromedio('Promedio:')
            f.write('{},{},{},{},{} \n'.format(Numero_de_Cuenta,Nombre,Edad,Carrera,Promedio))
            f.close()
        except IOError as e:
            print('Error al abrir el archivo -- ',e.errno)
        #con esto ya se crea el archivo y ya se pueden guardar datos para que no se borren al cerrar el programa 
        
    elif opc==2:
        try:
            f=open('DOCALUMNOS.txt','r') 
            datos=f.readlines() #trae la informacion en una lista y no es una cadena 
            existe1=True
            f.close()
        except IOError as e:
            print('Error al abrir el archivo---',e.errno)
            existe1=False

        if existe1==True:
            Id=leer.leercuenta('Id del usuario:')
            existe,indice = Buscar_Archivos(datos,Id)   #necesitamos una funcion para bcuscar archivos 
            if existe==True:
                datos.pop(indice)
                try:
                    f=open('DOCALUMNOS.txt','w')             
                    f.writelines(datos)
                    f.close()                                            
                except IOError as e:
                    print('Error al abrir el archivo -- ',e.errno)
            else:
                print(Id,'No existe')
        
        
    elif opc==3:
        try:
            f=open('DOCALUMNOS.txt','r') 
            datos=f.readlines()
            existe1=True #Este nos permite saber si existe el archivo
            f.close()
        except IOError as e:
            print('Error al abrir el archivo---',e.errno)
            existe1=False  #Complementa el de arriba

        if existe1==True:
            Id=leer.leercuenta('Id del usuario:')
            existe,indice = Buscar_Archivos(datos,Id)
    
        if existe==True:
            print('{:<5s}{:<20s}{:<5s}{:<10s}{:<5s}'.format( #pasamos todo a cadenas 
            datos[indice],datos[indice],datos[indice],datos[indice],datos[indice][:indice])) 
        else:
            print(Id,' No existe ') 

    elif opc==4:
        try:
            f=open('DOCALUMNOS.txt','r') 
            datos=f.readlines()
            existe1=True #Este nos permite saber si existe el archivo
            f.close()
        except IOError as e:
            print('Error al abrir el archivo---',e.errno)
            existe1=False  #Complementa el de arriba

        if existe1==True:
            Id=leer.leercuenta('Id del usuario:')
            existe,indice = Buscar_Archivos(datos,Id)

        if existe:
            opc2=None
            while opc2!=6:
                menu2="""
                1. Nombre
                2. Edad
                3. Carrera
                4. Promedio
                5. Volver
                """
                print(menu2)
                opc2=leer.leerentero('Que deseas modificar')
                if opc2==1:
                    print(datos[indice])
                    
                elif opc2==2:
                    Edad=leer.leeredad('Digite la nueva Edad:')  
                    f.write('{} \n'.format(Edad))
                elif opc2==3:
                    Carrera=(input('Digite la nueva Carrera:'))
                    f.write('{} \n'.format(Carrera))
                elif opc2==4:
                    Promedio=leerpromedio('Digite el nuevo Promedio:')
                    f.write('{} \n'.format(Promedio))
                elif opc2==5:
                    print('Fue un placer atenderle')             
        else:
            print(Id,'No existe el alumno ')    
            
    elif opc==5:
        os.system('cls')
        try:
            f=open('DOCALUMNOS.txt','r') 
            datos=f.readlines() #trae la informacion en una lista y no es una cadena 
            f.close()
            for i in datos:
                a=i.split(',')
                print('{:<5s}{:<20s}{:<5s}{:<10s}{:<5.2f}'.format( #pasamos todo a cadenas 
                a[0],a[1],a[2],a[3],float(a[4][:-1])))  #[:-1] esto es para eliminar el salto de linea que se tiene al llenar el dato 
        except IOError as e:
            print('Error al abrir el archivo---',e.errno)

    elif opc==6:
        print('Regrese pronto, fue un placer atenderle')
    else:
        print('Dato no valido')

