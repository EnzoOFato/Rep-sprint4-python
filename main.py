# todos imports para o funcionamento do programa
import os
from mensagens import *
from contagem import Contagem
from crud import *

# declaração do objeto contagem, que será usado para contagem regressiva de 3 segundos
contagem = Contagem(3)

while True:
    os.system("cls") # comando para limpar o cmd
    escolha = mensagem_incial()
    match escolha: 
        case 1:
            consultar_jogadoras_alfa()
            input(continuar())
        case 2:
            consultar_jogadora_id()
            input(continuar())
        case 3:
            cadastrar_jogadora()
            contagem.contar()
        case 4:
            atualizar_jogadora()
            contagem.contar()
        case 5:
            deletar_jogadora()
            contagem.contar()
        case 6:
            consultar_jogadora_id()
            input(continuar())
        case 7:
            mensagem_final()
            contagem.contar()
            break
        case _:
            mensagem_erro()