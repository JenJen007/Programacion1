# Importa las clases  Is_Mutant  desde sus respectivos archivos.
from Es_Mutante import Is_Mutant

if __name__  == "__main__":
    dna = []
    print("Ingrese las letras del adn a analizar: ")
    for _ in range(6):
        dna.append(input().upper())

    if Is_Mutant.is_mutant(dna):
        print("Es mutante")
    else:
        print("No es mutante")    
