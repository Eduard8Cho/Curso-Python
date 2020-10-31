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

Nombre=[]
Edad=[]
Carrera=[]
Promedios=[]
numcuenta=[]

while opc!=6:
    print(menu)
    opc=int(input('Digita una opcion:'))

    if opc==1:
        numcuenta.append(len(numcuenta)+1)
        Nombre.append(input('Nombre:'))
        Edad.append(int(input('Edad:')))
        Carrera.append(input('Carrera:'))
        Promedios.append(float(input('Promedio:')))
    elif opc==2:
        #hay dos tipos de baja fisica y logica 
        #fisica se borra del arreglo y no puede regresar 
        #logica existe pero se puede volver a activar 
        #baja fisica 

        nC=int(input('Id del usuario:'))
        existe=False
        for  i in range(0,len(numcuenta)):
            if numcuenta[i]==nC:
                existe=True
                break
            
        if existe:
            Nombre.pop(i)
            Edad.pop(i)
            Carrera.pop(i)
            Promedios.pop(i)
            numcuenta.pop(i)
        else:
            print(nC,'No existe') 



    elif opc==3:
        nC=int(input('Id del usuario:'))
        existe=False
        for  i in range(0,len(numcuenta)):
            if numcuenta[i]==nC:
                existe=True
                break
            
        if existe:
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                numcuenta[i],Nombre[i],Edad[i],Carrera[i],Promedios[i]))
        else:
            print(nC,'No existe') 

    elif opc==4:
        nC=int(input('Id del usuario:'))
        existe=False
        for  i in range(0,len(numcuenta)):
            if numcuenta[i]==nC:
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
                opc2=int(input('Que deseas modificar'))
                if opc2==1:
                    Nombre[i]=input('Dame el nuevo nombre')
                elif opc2==2:
                    Edad[i]=int(input('Dame el nuevo nombre'))
                elif opc2==3:
                    Carrera[i]=input('Dame el nuevo nombre')
                elif opc2==4:
                    Promedios[i]=int(input('Dame el nuevo nombre')) 
                elif opc2==5:
                    print('Fue un placer atenderle')             

        else:
            print(nC,'No existe')    
            


    elif opc==5:
        for i in range(0,len(Nombre)):
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                numcuenta[i],Nombre[i],Edad[i],Carrera[i],Promedios[i]))
    elif opc==6:
        pass
    else:
        print('Dato no valido')

