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
        if a['numcuenta']==nC:
            existe=True
            break
    return existe,indice













while opc!=6:
    print(menu)
    opc=leer.leerentero('dame una opcion')

    if opc==1:
        a={}
        try:
            f=open('alumnos.txt','r')
            nCta=int(1)
            Nombre=(input('Nombre:'))
            Edad=leer.leeredad('Edad:')
            Carrera=(input('Carrera:'))
            Promedio=leerpromedio('Promedio:')
            f.write('{},{},{},{}\n'.format(nCta,Nombre,Edad,Carrera,Promedio))
            f.close()
        except IOError as e:
            print('Error al arbir el archivo --',e.errno)
      
    elif opc==2:
        #hay dos tipos de baja fisica y logica 
        #fisica se borra del arreglo y no puede regresar 
        #logica existe pero se puede volver a activar 
        #baja fisica 
        nC=leerentero('Id del usuario:')
        existe,indice == buscar(existe,nC)
            
        if existe:
            alumnos.pop(r[1])
        else:
            print(nC,'No existe') 



    elif opc==3:
        nC=leerentero('Id del usuario:')
        existe=False
        for  i in alumnos:
            if i['numcuenta']==nC:
                existe=True
                break
            
        if existe:
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                i['numcuenta'],i['Nombre'],i['Edad'],i['carrera'],i['Promedio']))
        else:
            print(nC,'No existe') 

    elif opc==4:
        nC=leerentero('Id del usuario:')
        existe=False
        for  i in alumnos:
            if i['numcuenta']==nC:
                existe=True
                break

        if existe:
            opc2=None
            while opc2!=6:
                menu2="""
                    MENU 
                    1. Nombre 
                    2. Edad 
                    3. Carrera 
                    4. Promedio
                    5. Salir
                    """
                print(menu2)
                opc2=leerentero('Que deseas modificar')
                if opc2==1:
                    i['Nombre']=input('Dame el nuevo nombre')
                elif opc2==2:
                    i['Edad']=leeredad('Dame el nuevo nombre')
                elif opc2==3:
                    i['Carrera']=input('Dame el nuevo nombre')
                elif opc2==4:
                    i['Promedio']=leerpromedio('Dame el nuevo nombre')
                elif opc2==5:
                    print('Fue un placer atenderle')             

        else:
            print(nC,'No existe')    
            


    elif opc==5:
        try:
            f=open('alumnos.txt','r')
            datos=f.readlines()
            for i in alumnos:
                print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                    i[0],i[1],i[2],i[3],i[4]))
           
            f.close()
        except IOError as e:
            print('Error al arbir el archivo --',e.errno)


        if datos==None:
            pass
        else:
            for i in datos: 
                #print(i[:-1])
                print(i,end="")




        for i in alumnos:
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                i['numCuenta'],i['Nombre'],i['Edad'],i['Carrera'],i['Promedio']))
    elif opc==6:
        pass
    else:
        print('Dato no valido')

