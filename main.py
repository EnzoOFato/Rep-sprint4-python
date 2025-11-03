import os
from mensagens import *
from contagem import Contagem
from crud import *

contagem = Contagem(3)

while True:
    os.system("cls")
    escolha = mensagem_incial()
    if escolha == 1:
        consultar_jogadoras_alfa()
        input("Continuar ")
    elif escolha == 2:
        cadastrar_jogadora()
        contagem.contar()
    elif escolha == 3:
        atualizar_jogadora()
        contagem.contar()
    elif escolha == 4:
        pass
    elif escolha == 5:
        pass
    elif escolha == 6:
        mensagem_final()
        contagem.contar()
        break
    else:
        mensagem_erro()