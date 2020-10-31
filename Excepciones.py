#Exepcion es un error
try:
    num=int(input('Dame un nuemero: '))
    print (5/num)
except ValueError:
    print('No es un entero')
except ZeroDivisionError:
    print('no se puede dividir entre cero')
except:
    print('algo salio mal')

print('continua')    


error = False
while not error:
    try:
        num=int(input('Dame un nuemero: '))
        print (5/num)
        error=True
    except ValueError:
        print('No es un entero')
    except ZeroDivisionError:
        print('no se puede dividir entre cero')
    except:
        print('algo salio mal')
