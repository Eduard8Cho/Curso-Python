def leerentero(opc):
    error = False
    while not error:
        try:
            n=int(input('Digita una opcion:'))
            error=True
        except ValueError:
            print('¡¡DATO NO VALIDO!!')
    return n

def leerpromedio(dato):
    error = False
    while not error:
        try:
            n=float(input('Promedio:'))
            error=True
        except ValueError:
            print('¡¡DATO NO VALIDO!!')
    return n

def leeredad(dato):
    error = False
    while not error:
        try:
            n=int(input('Edad:'))
            error=True
        except ValueError:
            print('No es un entero')
    return n

def leercuenta(opc):
    error = False
    while not error:
        try:
            n=int(input('Digita la cuenta del alumno:'))
            error=True
        except ValueError:
            print('¡¡DATO NO VALIDO!!')
    return n