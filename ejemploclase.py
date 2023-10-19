from funciones import *
while True:   
    num = int(input("Ingrese un número: "))
    if num == 0 :
        break
    print(f'La sumatoria de los dígitos ingresados es: {sumatoria(num)}')
    num += sumatoria(num)
    print (num)