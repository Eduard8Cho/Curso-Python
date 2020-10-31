try:
            f=open('DOCUMENTOS.txt','r')
            datos=f.readlines()
            existe1=True #Este nos permite saber si existe el archivo
            f.close()
        except IOError as e:
            print('Error al abrir el archivo---',e.errno)
            existe1=False  #Complementa el de arriba

        if existe1==True:

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