import random
"""Ejercicio 1
frase = input("Ingrese una frase: ").title()
if len(frase) == 4:
    print(f'{frase}!')
else: 
    print(f'{frase}?')"""
"""words = ["Hola","Fruta","Casa","Perro","Gato"]
word = random.choice(words)
aux = 5
while(aux > 1):
    letter = input("Ingresa la letra de la palabra que desea encontrar: ")
    if word[0] == letter:
        letter = input("Ingresa otra letra:  ")"""

string = input("Ingrese una palabra: ")
word_long = len(string)
print(f'En la cadena {string} hay {word_long} caracteres')        