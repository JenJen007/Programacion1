

import random

#Pedir al usuario que ingrese su nombre para empezar el juego

name_user = input("Hola! decime tu nombre asi empezamos a jugar: ")

#Genera números aleatorios entre 1 y 50
number_random = random.randint(1, 50)


print(f"Hola {name_user} este juego se trata de encontrar el numero oculto entre el 1 y 50. Tenes 7 intentos.")
#Pide el primer número
number = int(input(f"{name_user} ingresa el primer numero para empezar a jugar: "))

aux = 7
#Comprueba el auxiliar en caso de que llegue a 1 se termina el programa y en caso de que encuentre el número se termina el programa
while(aux > 1):
    
    if number == number_random:
        print(f"Felicidades {name_user} encontraste el numero oculto. !Fin del juego!")
        break
    elif number > number_random:
        print(f"{name_user} el numero que ingresaste es mayor al numero oculto.")  
        aux -= 1
        number = int(input(f"Proba con otro numero, te quedan {aux} intentos: "))
        print("")
    else:
        print(f"{name_user} el numero que ingresaste es menor al numero oculto.")  
        aux -= 1 
        number = int(input(f"Proba con otro numero, te quedan {aux} intentos: "))
        print("")
#Comprueba auxiliar que si es igual a 1 imprime un mensaje
if aux == 1:
    print("El numero oculto era: ", number_random)
    print(f"Suerte {name_user} para la próxima!")






























































