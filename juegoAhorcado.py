import random

#Se crea funcion que crea una lista de palabras y llama a la funcion randmon para elegir una palabra aleatoriamente
def obtain_word():
    words=["perro","gato","mariposa","murcielago","colibri","guacamayo","caballo","loro"]
    word=random.choice(words)
    print("La palabra a adivinar tiene ", len(word), " letras: ")
    return word
#Funcion que contiene como parametro la palabra que se debe adivinar y una lista con las letras que se adivinaron correctamente
def show_board(secret_word,guess_letters):
    board=""
    #bucle para recorrer cada letra de palabra a adivinar y se valida si existe se agrega y sino se muestra un guion bajo
    for letter in secret_word:
        if letter in guess_letters:
            board+=letter
        else:
            board+="_"
            print(board)
#Funcion para jugar el juego. Llamamos a otra funcion para que me devuelva la palabra a adivinar
def play_hangman():
    secret_word = obtain_word()
    #Crea lista de palabras y se llenara con las letras adivinadas
    guess_letters = []
    tries=6
    print("Bienvenido al juego del ahorcado: ")
    print("-------------------")
    name=input("Ingrese su nombre para empezar el juego: ").title()
    
#Bucle que recorrera mientras existan intentos
    while tries > 0:
        show_board(secret_word,guess_letters)
        letter=input("Ingrese una letra: ").lower()

        #Compara que la letra exista en la lista de letras adivinadas
        if letter in guess_letters:
            print("Ya ingresó esa letra. Pruebe con otra.")
            continue #Saltea pasos del bucle y vuelve al principio
        #Si la letra no está en la lista de palabras adivinadas probamos que esté en la palabra secreta y la agregamos a la lista
        if letter in secret_word:
            guess_letters.append(letter)
            #Comprueba que secret_word y guess_letters son iguales creando un conjunto. 
            if set(guess_letters) == set(secret_word):
                print(f'Felicidades {name}, has acertado la palabra: {secret_word}')
                break
        else:
            tries -= 1
            print(f'Letra incorrecta. {name} te quedan {tries} intentos.')
    #Si no se adivina la palabra muestra un mensaje
    if tries == 0:
        print(f'Lo siento {name}. Has perdido. La palabra secreta era: {secret_word}')           

play_hangman()        