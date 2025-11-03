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
    elif escolha == 3:
        cadastrar_jogadora()
        contagem.contar()
    elif escolha == 4:
        atualizar_jogadora()
        contagem.contar()
    elif escolha == 5:
        deletar_jogadora()
        contagem.contar()
    elif escolha == 6:
        pass
    elif escolha == 7:
        mensagem_final()
        contagem.contar()
        break
    else:
        mensagem_erro()