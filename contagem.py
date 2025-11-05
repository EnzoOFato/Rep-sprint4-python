import time # Import da biblioteca time para usar a função sleep

# Classe contagem para realizar a contagem regressiva
class Contagem:
    def __init__(self, tempo):
        self.tempo = tempo
    def contar(self):
        for i in range(self.tempo):
            print(".", end="")
            time.sleep(1)