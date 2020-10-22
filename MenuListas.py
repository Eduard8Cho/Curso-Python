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

while opc!=6:
    print(menu)
    opc=int(input('Digita una opcion:'))

    if opc==1:
        Nombre.append(input('Nombre:'))
        Edad.append(int(input('Edad:')))
        Carrera.append(input('Carrera:'))
        Promedios.append(int(input('Promedio:')))
    elif opc==2:
        pass
    elif opc==3:
        pass
    elif opc==4:
        pass
    elif opc==5:
        for i in range(0,len(Nombre)):
            print((Nombre[i],Edad[i],Carrera[i],Promedios[i]))
    elif opc==6:
        pass
    else:
        print('Dato no valido')

        