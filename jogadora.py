# Classe que representa uma jogadora
# Essa abordagem facilita a manipulação dos dados das jogadoras no programa
class Jogadora:
    def __init__(self, id ,nome, idade, clube, bpm, velocidade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.clube = clube
        self.bpm = bpm
        self.velocidade = velocidade