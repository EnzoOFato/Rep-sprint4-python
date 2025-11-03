import os
from mensagens import *
from contagem import Contagem

jogadoras = {}
contagem = Contagem(3)

while True:
    os.system("cls")
    escolha = mensagem_incial()
    if escolha == 1:
        pass
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass
    elif escolha == 4:
        pass
    elif escolha == 5:
        pass
    elif escolha == 6:
        print("Até logo")
        contagem.contar()
        break
    else:
        print("Escolha uma opção correta")