import random
"""Ejercicio 1
frase = input("Ingrese una frase: ").title()
if len(frase) == 4:
    print(f'{frase}!')
else: 
    print(f'{frase}?')"""

"""Ejercicio 2
words = ["hola","fruta","casa","perro","gato"]
word = random.choice(words)
max_tries = 5
tries = 0
guess = ["_"]*len(word)
print("Bienvenido al juego de adivina la palabra.")
print("La palabra a adivinar tiene ", len(word), " letras.")
while(tries < max_tries):
    letter = input("Ingresa la letra de la palabra que desea encontrar: ").lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guess[i] = letter
        print("¡Bien hecho! La palabra hasta ahora es: ", "".join(guess))
    else:
        tries += 1
        print("Letra incorrecta. Intentos restantes:", max_tries - tries)
    if "".join(guess) == word:
        print(f'¡Felicidades! Has adivinado la palabra: {word}')
        break
else:
    print(f"¡Agotaste tus intentos! La palabra era: {word}")"""

"""Ejercicio 3
string = input("Ingrese una palabra: ")
word_long = len(string)
print(f'En la cadena {string} hay {word_long} caracteres')        
"""
"""Ejercicio 4 
# Solicitar al usuario ingresar el sueldo base, la asistencia de lunes a viernes y las horas trabajadas los domingos
salary = float(input("Ingrese el sueldo base del empleado: "))
work_mon_fri = input("¿El empleado asistió todo el mes de lunes a viernes? (Sí/No): ").lower()
hours_sunday = int(input("Ingrese las horas trabajadas los domingos: "))

# Inicializar el monto adicional en 0
additional = 0

# Calcular el monto adicional basado en las condiciones dadas
if work_mon_fri == "si":
    if hours_sunday >= 3 and hours_sunday <= 5:
        additional = salary * 0.03
    elif hours_sunday >= 6 and hours_sunday <= 10:
        additional = salary * 0.10
elif work_mon_fri == "no" and hours_sunday >= 3 and hours_sunday <= 10:
    additional = salary * 0.02

# Calcular el salario total
total_salary = salary + additional

# Mostrar el salario total
print("El salario total del empleado es:", total_salary)
"""
"""Ejercicio 5
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

if num1 == num2:
    total = num1*num2
    print(f'El resultado es {total}')
elif num1 > num2:
    total = num1 - num2
    print(f'El resultado es {total}')
else: 
    total = num1 + num2
    print(f'El resultado es {total}')
"""
"""Ejercicio 6
age = int(input("Ingrese su edad: "))
antique = int(input("Ingrese la antigüedad de su empleo: "))
if age >= 60 and antique < 25:
    print(f'Usted estará adscrito a la jubilación por edad.')
elif age < 60 and antique >= 25:
    print(f'Usted estará adscrito a la jubilación por antigüedad joven.')
elif age >= 60 and antique >= 25:
    print(f'Usted estará adscrito a la jubilación por antigüedad adulta.')
else:
     print("La persona no cumple con los requisitos para ninguna jubilación en 2010.")
"""
"""Ejercicio 7
"""
salary = float(input("Ingrese su salario: "))
antique = int(input("Ingrese la antigüedad en su empleo: "))
utility = 0
if antique <= 1:
    utility = salary * 0.05
    anual_salary = (salary + utility) * 12
    print(f"El empleado recibe anual un total de ${anual_salary}")
elif antique > 1 and antique <= 2:
    utility = salary * 0.07
    anual_salary = (salary + utility) * 12
    print(f"El empleado recibe anual un total de ${anual_salary}")
elif antique > 2 and antique <= 5:
    utility = salary * 0.10
    anual_salary = (salary + utility) * 12
    print(f"El empleado recibe anual un total de ${anual_salary}")
elif antique > 5 and antique <= 10:
    utility = salary * 0.15
    anual_salary = (salary + utility) * 12
    print(f"El empleado recibe anual un total de ${anual_salary}")
elif antique >10:
    utility = salary * 0.20
    anual_salary = (salary + utility) * 12
    print(f"El empleado recibe anual un total de ${anual_salary}")