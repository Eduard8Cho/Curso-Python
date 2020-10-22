import os
import math

os.system('cls')
op=0
while op!=6:
    
    print('1.- Hola Mundo')
    print('2.- Area de Triangulo')
    print('3.- Salario del Trabajador')
    print('4.- Ecuacion Cuadratica')
    print('5.- Rango')
    print('6.- Salir')

    op=int(input('Digita una opcion: '))

    if op==1:
        print("hola mundo")
        print("Mi primer programa en python")
    elif op==2:
        a=int(input('Digita el lado a: '))
        b=int(input('Digita el lado b: '))
        c=int(input('Digita el lado c: '))

        #Operadores Aritmeticos: " +,-,*,/,//,%(reciduo),**(potencia) "
        #Operadores Relacionales: " >,<,<=,>=,==,!= "
        #Operadores Logicos: "and,or,not"
        #Operadores Especiales:

        s=(a+b+c)/2

        A=math.sqrt(s*(s-a)*(s-b)*(s-c))

        print('El area es: ',A) #con muchos decimales 
        print('El area es: %.2f'%A) #con el numero de decimales indicados (solo una forma hay muchas mas)
        print('El triangulo de lado %d,%d,%d tiene un area de: %.2f'%(a,b,c,A)) #inprimir varias variablels al mismo tiempo

    elif op==3:
        nombre=input('Nombre:')
        ht=int(input('Horas trabajadas: '))
        ph=float(input('Pago por hora: '))
        salario=ht*ph
        print('El salario de ',nombre,'es $',salario)
    elif op==4:
        a=int(input('Dame el valor de a: '))
        b=int(input('Dame el valor de b: '))
        c=int(input('Dame el valor de c: '))

        if (a!=0):

            if(b**2-4*a*c)<0:
                print('La raiz imaginaria y no se puede calcular')
            else:   
                x1=(-b+(math.sqrt(b**2-4*a*c)))/(2*a)
                x2=(-b-(math.sqrt(b**2-4*a*c)))/(2*a)
                print('x1=',x1,'\nx2=',x2)

        else:
            print('Debido a que a es 0 la ecuacion no es cuadratica')
    elif op==5:
        n=int(input('Numero entre 0 y 30: ')) 

        if n>=0 and n<=10:
            print('Esta e el rango del 0 al 10')
        else:
            if n>10 and n<=20:
                print('Esta en el rango del 11 al 20')
            else:
                if n>20 and n<=30:
                    print('Esta en el rango del 21 al 30')
                else:
                    print('El numero es mayor que 30')
    elif op==6:
        print('Fue un placer atenderle ')
    else:
        print('dato erroneo')




