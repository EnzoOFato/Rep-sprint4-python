import time

class Contagem:
    def __init__(self, tempo):
        self.tempo = tempo
    def contar(self):
        for i in range(self.tempo):
            print(".", end="")
            time.sleep(1)