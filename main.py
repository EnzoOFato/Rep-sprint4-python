# todos imports para o funcionamento do programa
import os
from mensagens import *
from contagem import Contagem
from crud import *

# declaração do objeto contagem, que será usado para contagem regressiva de 3 segundos
contagem = Contagem(3)

while True:
    os.system("cls") # comando para limpar o cmd
    escolha = mensagem_incial() # chamada da função que exibe o menu inicial e recebe a escolha do usuário
    # Estrutura match case para tratar a escolha do usuário. (mais legível que laços condicionais)
    match escolha: 
        case 1:
            consultar_jogadoras_alfa()
            input(continuar()) # Pausa para o usuário ver o resultado antes de limpar a tela
        case 2:
            consultar_jogadora_id()
            input(continuar()) # Pausa para o usuário ver o resultado antes de limpar a tela
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
            input(continuar()) # Pausa para o usuário ver o resultado antes de limpar a tela
        case 7:
            mensagem_final()
            contagem.contar()
            break
        # Escolha case default para opções inválidas
        case _:
            mensagem_erro()

# Explicação de cada função em seu respectivo arquivo .py