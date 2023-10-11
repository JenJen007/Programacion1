#Creamos un diccionario que contenga el abecedario
alpha = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',
         14:'ñ',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
#Solicitamos como correrá cada palabra
running = int(input("Ingrese la cantidad de lugares que correran las letras: "))
#Creamos una lista que contenga los mensajes encriptados
menssages =[]
#Con un ciclo recorremos cada mensaje ingresado
for i in range(5):
    menssage = input(f"\nIngrese el mensaje de encriptado {i+1}: ").lower() 
    menssage_encrip = ""

    for letter in menssage:
        if letter.isalpha():
            mayus = letter.isupper()
            letter = letter.lower()
            if letter in alpha.values():
                index = [k for k, v in alpha.items() if v == letter][0]
                new_index = (index + running)%27
                new_letter = alpha.get(new_index)
                print(new_letter,end=" ")
                if mayus:
                    new_letter = new_letter.upper()
                menssage_encrip += new_letter
        else:   
            menssage_encrip += letter     
menssages.append(menssage_encrip)

for i, menssage_encrip in enumerate(menssages):
    print(f"Mensaje {i+1} encriptado: {menssage_encrip}")