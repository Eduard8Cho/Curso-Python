
i=0
num=[]
n=int(input('Cuantos numeros deseas leer:   '))
while i<n:
    #num.append(i)
    num.append(int(input('Digita un numero: ')))
    i+=1

#print(num)

#for i in num:
 #   print(i)

for i in range(0,len([num])):
    print(num[i])