# Importa las clases Human y Check_DNA desde sus respectivos archivos.
from Human import Human
from ComprobarDNA import Check_DNA

# Define la clase Is_Mutant con un método para verificar si un ADN es mutante.
class Is_Mutant:
    @staticmethod
    def is_mutant(dna):
# Crear una instancia de la clase Human con valores para dna e is_mutant
        h = Human(dna="dna_value",is_mutant=True)  # Reemplaza "dna_value" por el valor real del ADN y True/False según corresponda
        det = Check_DNA()
        DNA = det.convert_list(dna)
        if not det.check_matrix(DNA):
            return False
        aux = 0
        aux = det.run_diagonal(DNA,aux)
        aux = det.run_vertical(DNA,aux)
        aux = det.run_horizontal(DNA,aux)
        aux = det.run_inverse_diagonal(DNA,aux)
        if aux >=2:
            h.is_mutant = True
            h.dna = str(DNA)
            return True
        h.is_mutant = False
        h.dna = str(DNA)
        return False
    