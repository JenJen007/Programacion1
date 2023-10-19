from funciones import *
aux=0
while True:   
    num = int(input("Ingrese un número: "))
    if num == 0 :
        break
    print(f'La sumatoria de los dígitos ingresados es: {sumatoria(num)}')
    aux += num
    
print(f'El total de los valores ingresados hasta ahora es {aux}')
print(f'La sumatoria de todos los valores sería {sumatoria(aux)}')