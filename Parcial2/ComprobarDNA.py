
# Define la clase Check_DNA con varios métodos para verificar el ADN.
class Check_DNA:

# Convierte una lista en otra lista (en realidad, no hace ningún cambio).
    def convert_list(self,dna):
        return list(dna)
    
# Verifica si la matriz cumple con varias condiciones.
    def check_matrix(self,dna):
        if not (self.check_square_matrix(dna) and self.check_letters_matrix(dna) and self.check_min_size(dna)):
            return False
        return True
    
# Verifica si la matriz es cuadrada (mismo número de filas y columnas).    
    def check_square_matrix(self,dna):
        for row in dna:
            if len(row) != len(dna):
                return False
        return True
    
# Verifica si todas las letras en la matriz son A, T, C o G.    
    def check_letters_matrix(self,dna):
        for s in dna:
            if not s.isalpha() or not set(s).issubset("ATCG"):
                return False
        return True
    
# Verifica si el tamaño de la matriz es mayor o igual a 4x4.    
    def check_min_size(self,dna):
        if len(dna) < 4:
            return False
        return True
    
# Compara cuatro letras y devuelve True si son iguales.    
    def compare_letters(self,A,B,C,D):
        return A == B == C == D
    
# Realiza un análisis diagonal en la matriz.    
    def run_diagonal(self,dna,aux):
        for i in range(len(dna)-3):
            for j in range(len(dna[i])-3):
                if self.compare_letters(dna[i][j],dna[i+1][j+1],dna[i+2][j+2],dna[i+3][j+3]):
                    aux += 1
                    if aux == 2:
                        return aux
        return aux
    
# Realiza un análisis vertical en la matriz.    
    def run_vertical(self,dna,aux):
        if aux >= 2:
            return aux
        for i in range(len(dna)-3):
            for j in range(len(dna[i][0])):
                if self.compare_letters(dna[i][j],dna[i+1][j],dna[i+2][j],dna[i+3][j]):
                    aux += 1
                    if aux == 2:
                        return aux
        return aux
    
# Realiza un análisis horizontal en la matriz.    
    def run_horizontal(self,dna,aux):
        if aux >= 2:
            return aux
        for i in range(len(dna)):
            for j in range(len(dna[i])-3):
                if self.compare_letters(dna[i][j],dna[i][j+1],dna[i][j+2],dna[i][j+3]):
                    aux +=1
                    if aux == 2:
                        return aux
        return aux      

# Realiza un análisis de la diagonal inversa en la matriz.          
    def run_inverse_diagonal(self,dna,aux):
        if aux >=2:
            return aux
        for i in range(len(dna)-3):
            for j in range(len(dna[i][0])-1,len(dna[i][0])-2,-1):
                if self.compare_letters(dna[i][j],dna[i+1][j-1],dna[i+2][j-2],dna[i+3][j-3]):
                    aux += 1
                    if aux == 2:
                        return aux
        return aux                      
                    

