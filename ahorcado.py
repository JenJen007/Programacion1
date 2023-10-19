
import random
#Se crea una lista con temática en hardware
words = ["mouse","monitor","teclado","gabinete","motherboard","usb","driver","memoria externa"]
#Elije al azar una palabra de la lista
word = random.choice(words)
#Se inicializa variables
max_tries = 10
tries = 0
#Depende de la longitud de palabra marca un guión bajo
guess = ["_"]*len(word)
#Se entra al juego
print("Bienvenido al juego del ahorcado: ")
print("-------------------")
print("La palabra a adivinar tiene ", len(word), " letras: ")
print("-------------------")
#Se evalúa que queden intentos para entrar al ciclo
while(tries < max_tries):
    letter = input("Ingresa la letra de la palabra que desea encontrar: ").lower()
#Se evalúa que la letra ingresada exista en la palabra elegida, si existe compara las posiciones
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guess[i] = letter
                #Con la función join() va uniendo las letras ingresadas y las muestra
        print("¡Bien hecho! La palabra hasta ahora es: ", "".join(guess))
    else:
        #Incrementa la variable de intentos y resta a la variable de máximos intentos
        tries += 1
        print("Letra incorrecta. Intentos restantes:", max_tries - tries)
        #Si se termina la palabra y es igual a la elegida se muestra por pantalla con un mensaje de éxito
    if "".join(guess) == word:
        print(f'¡Felicidades! Has adivinado la palabra: {word}')
        break
else:
    print(f"¡Agotaste tus intentos! La palabra era: {word}")