from jogadora import Jogadora
from mensagens import *
from arquivos import *

jogadoras = ler_jogadoras()

def cadastrar_jogadora():
    global jogadoras
    dados = mensagem_cadastro()

    if jogadoras:
        novo_id = int(jogadoras[-1].id) + 1
    else:
        novo_id = 1

    jogadora = Jogadora(str(novo_id), *dados)
    escrever(jogadora)
    print("\nJogadora cadastrada com sucesso!")
    jogadoras = ler_jogadoras()

def consultar_jogadoras_alfa():
    jogadoras_ordenadas = sorted(jogadoras, key=lambda x: x.nome)
    print("\nLista de Jogadoras (ordem alfabética):")
    for jogadora in jogadoras_ordenadas:
        mesagem_visualizacao(jogadora)

def consultar_jogadora_id():
    jogadoras_ordenadas = sorted(jogadoras, key=lambda x: x.id)
    print("\nConsulta de Jogadora por ID")
    for jogadora in jogadoras_ordenadas:
        mesagem_visualizacao(jogadora)

def atualizar_jogadora():
    try:
        global jogadoras
        jogadoras = ler_jogadoras()
        id = mensagem_id("atualizada")
        jogadora_antiga = None

        for jogadora in jogadoras:
            if jogadora.id == id:
                jogadora_antiga = jogadora
                break

        if not jogadora_antiga:
            raise ValueError

        dados = mensagem_atualizacao(jogadora_antiga)
        jogadora_antiga.bpm, jogadora_antiga.velocidade = dados

        sobrescrever_arquivo(jogadoras)
        
        print("\nJogadora atualizada com sucesso!")
        jogadoras = ler_jogadoras()
    except (ValueError, IndexError):
        print("\nID inválido. Digite um número válido.")

def deletar_jogadora():
    try:
        global jogadoras
        id = mensagem_id("deletada")
        index = int(id) -1

        if index < 0 or index >= len(jogadoras):
            raise IndexError
        
        jogadoras.pop(index)
        sobrescrever_arquivo(jogadoras)

        print("\nJogadora deletada com sucesso!")
        jogadoras = ler_jogadoras()
    except (ValueError, IndexError):
        print("\nID inválido. Digite um número válido.")

def consultar_jogadora_id():
    try:
        id = mensagem_id("consultada")
        jogadora_encontrada = None

        for jogadora in jogadoras:
            if jogadora.id == id:
                jogadora_encontrada = jogadora
                break

        mesagem_visualizacao(jogadora_encontrada)
    except ValueError:
        print("\nID inválido. Digite um número válido.")