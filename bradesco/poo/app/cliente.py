# Define uma classe
class Cliente: 
    def __init__(self, n, fone): #define a função e os atributos

        self._nome = n #define cada atributo
        self._telefone = fone

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome