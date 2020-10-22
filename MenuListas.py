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
        pass
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
        pass
    elif opc==5:
        for i in range(0,len(Nombre)):
            print('{:<5d}{:<20s}{:<5d}{:<10s}{:<15.2f}'.format(
                numcuenta[i],Nombre[i],Edad[i],Carrera[i],Promedios[i]))
    elif opc==6:
        pass
    else:
        print('Dato no valido')

