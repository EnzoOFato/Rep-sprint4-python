class Jogadora:
    def __init__(self, nome, idade, clube, bpm, velocidade):
        self.nome = nome
        self.idade = idade
        self.clube = clube
        self.bpm = bpm
        self.velocidade = velocidade
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Clube: {self.clube}, BPM: {self.bpm}, Velocidade: {self.velocidade}"