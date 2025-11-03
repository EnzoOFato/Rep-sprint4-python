from jogadora import Jogadora
from mensagens import *
from arquivos import *

jogadoras = ler_jogadoras()

def cadastrar_jogadora():
    global jogadoras
    dados = mensagem_cadastro()
    jogadora = None
    for i in range(len(dados)):
        jogadora = Jogadora(len(jogadoras)+1,*dados)
    escrever(jogadora)
    print("\nJogadora cadastrada com sucesso!")
    jogadoras = ler_jogadoras()

def consultar_jogadoras_alfa():
    jogadoras_ordenadas = sorted(jogadoras, key=lambda x: x.nome)
    print("\nLista de Jogadoras (ordem alfabética):")
    for jogadora in jogadoras_ordenadas:
        mesagem_visualizacao(jogadora)

def atualizar_jogadora():
    try:
        global jogadoras
        id = mensagem_id("atualizada")
        index = id -1
        jogadoras.pop(index)
        dados = mensagem_atualizacao()
        jogadora_atualizada = Jogadora(id, jogadoras[index].nome, jogadoras[index].idade, jogadoras[index].clube, *dados)
        jogadoras.insert(index, jogadora_atualizada)
        sobrescrever_arquivo(jogadoras)
        print("\nJogadora atualizada com sucesso!")
    except (ValueError, IndexError):
        print("\nID inválido. Digite um número válido.")