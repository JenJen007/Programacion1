#Instrucciones del programa
"""
Realizar un programa que cumpla con las siguientes condiciones:
Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
Generar un menú de opciones, que serán:
Juego de números.
Juego de palabras.
Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
El mayor número par.
El promedio de los números impares.
Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
No olvides realizar las debidas validaciones!
"""
#Se pide al usuario que ingrese su nombre y se le saluda
username = input("Ingrese su nombre: ").capitalize()
print(f'Hola {username}!')

#Se usa un ciclo para mostrar el menú 
while True:
    print("Menú de opciones:")
    print("a) Juego de números")
    print("b) Juego de palabras")
    print("c) Salir")
    #El usuario ingresa la opcion que desea
    option = input(f"{username} elija una opción: ")
    #Se valida la opcion y se crea una lista
    if option == 'a':
        numbers = []
        
#Ciclo para pedir que se ingrese los números y contar si son pares o impares 
        while True:
            number_into = input(f'{username} ingresa un número entero (0 para salir): ')
            if number_into == '0':
                break
            if number_into.lstrip('-').isdigit():
                number = int(number_into)
                numbers.append(number)
            else:
                print(f'Por favor, {username} ingresa un número entero válido.')
#Variables para contabilizar
        pair_major = 0
        odd_sume = 0
        odd_count = 0
#Se valida que sean numeros pares ademas que no sean nulos y cual es el mayor
        for num in numbers:
            if num % 2 == 0:
                if pair_major is None or num > pair_major:
                    pair_major = num
            else:
                odd_sume += num
                odd_count += 1

        if pair_major is not None:
            print(f"El mayor número par es: {pair_major}")     
        else:
            print("No se ingresaron números pares.")
    #Se valida que la variable odd_count sea mayor a cero para contar los impares y calcular el promedio
        if odd_count > 0:
            odd_average = odd_sume / odd_count
            print(f"El promedio de los números impares es: {odd_average}")   
        else:
            print("No se ingresaron números impares.")            

        #Se valida la opcion b para que ingrese una frase y cuente las vocales de la frase y las muestre por pantalla
    elif option == 'b':
        sentence = input(f'{username} ingresa una frase: ').lower()
        vowels = 'aeiou'
        count_vowels = {vowel: sentence.count(vowel) for vowel in vowels}
        for vowel, quantity in count_vowels.items():
            print(f'La vocal "{vowel}" aparece {quantity} veces en la frase.')
            #Valida la opcion para salir del programa y muestra un mensaje de salida
    elif option == 'c':
        print(f'Hasta pronto {username}!')
        break
    else:
        print(f"Opción no válida. {username} elija 1,2 o 3.")                                    