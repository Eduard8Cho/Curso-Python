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




while opc!=6:
    print(menu)
    opc=leer.leerentero('Digita una Opcion')

    if opc==1:
        a={} #Declaramos el diccionario
        a['Numero_de_Cuenta']=int(len(alumnos)+1) #int len(alumnos+1): el nuemro de cuenta comienza en 1 pues el tamaño de alumnos al enrar vale cero
        a['Nombre']=(input('Nombre:')) #leemos en el key Nombre 
        a['Edad']=leer.leeredad('Edad:') #leer.leeredad para que solo lea numeros enteros y es leer. porque se llama asi la libreria leer.py
        a['Carrera']=(input('Carrera:'))
        a['Promedio']=leerpromedio('Promedio:')
        alumnos.append(a) #A la cadena alumnos le agregamos un valor por eso se usa append (a) que es el diccionario que creamos 
    elif opc==2:
        #hay dos tipos de baja fisica y logica 
        #fisica se borra del arreglo y no puede regresar 
        #logica existe pero se puede volver a activar 
        #baja fisica 
        Id=leer.leercuenta('Id del usuario:')
        existe,indice = buscar(alumnos,Id)

        if existe:
            alumnos.pop(indice) #indice nos devuelve el valor de la cadena en el que se quedo
        else:
            print(Id,' No existe ') 



    elif opc==3:
        Id=leer.leercuenta('Id del usuario:')
        existe,indice = buscar(alumnos,Id)
    
        if existe:
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                alumnos[indice]['Numero_de_Cuenta'],
                alumnos[indice]['Nombre'],
                alumnos[indice]['Edad'],
                alumnos[indice]['Carrera'],
                alumnos[indice]['Promedio'],))

        else:
            print(Id,' No existe ') 

    elif opc==4:
        Id=leer.leercuenta('Id del alumno:')
        existe,indice = buscar(alumnos,Id)
        if existe:
            opc2=None
            while opc2!=6:
                print(menu)
                opc2=leer.leerentero('Que deseas modificar')
                if opc2==1:
                    alumnos[indice]=input('Dame el nuevo nombre')
                elif opc2==2:
                    alumnos[indice]=leer.leeredad('Dame la nueva edad')
                elif opc2==3:
                    alumnos[indice]=input('Dame la nueva carrera')
                elif opc2==4:
                    alumnos[indice]=leerpromedio('Dame el nueo promedio')
                elif opc2==5:
                    print('Fue un placer atenderle')             
        else:
            print(Id,'No existe el alumno ')    
            
    elif opc==5:
        os.system('cls')
        for i in alumnos:
            #print('%-20s%-5d%-10s%-5.2f'%(nombres[i],edades[i],carreras[i],promedios[i]))
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<5.2f}'.format(
            i['Numero_de_Cuenta'],i['Nombre'],i['Edad'],i['Carrera'],i['Promedio']))
    elif opc==6:
        print('Regrese pronto, fue un placer atenderle')
    else:
        print('Dato no valido')

