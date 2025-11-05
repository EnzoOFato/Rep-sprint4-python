from jogadora import Jogadora # Importa a classe Jogadora para criar objetos jogadora
from mensagens import * # Importa as funções de mensagens para interagir com o usuário e retornar valores recebidos
from arquivos import * # Importa as funções de arquivos para manipular o arquivo de dados

jogadoras = ler_jogadoras() # Inicializa a lista de jogadoras com base no arquivo csv

# Função para cadastrar uma nova jogadora
def cadastrar_jogadora():
    global jogadoras # Declara que a variável jogadoras é global para modificar seu valor
    dados = mensagem_cadastro() # Chama a função que exibe a mensagem de cadastro e recebe os dados da nova jogadora

    # Gera um novo ID baseado no último ID existente
    if jogadoras:
        novo_id = int(jogadoras[-1].id) + 1
    else:
        novo_id = 1

    # Cria um novo objeto jogadora com os dados fornecidos
    jogadora = Jogadora(str(novo_id), *dados)
    # Armazena a nova jogadora no arquivo
    escrever(jogadora)
    print("\nJogadora cadastrada com sucesso!")
    jogadoras = ler_jogadoras() # Recarrega a lista de jogadoras atualizada

# Função para consultar todas as jogadoras em ordem alfabética
def consultar_jogadoras_alfa():
    jogadoras_ordenadas = sorted(jogadoras, key=lambda x: x.nome) # Ordena a lista de jogadoras pelo nome
    print("\nLista de Jogadoras (ordem alfabética):")
    # Exibe cada jogadora usando a função de mensagem de visualização
    for jogadora in jogadoras_ordenadas:
        mesagem_visualizacao(jogadora)

# Função para consultar todas as jogadoras em ordem crescente de ID
def consultar_jogadora_id():
    jogadoras_ordenadas = sorted(jogadoras, key=lambda x: x.id) # Ordena a lista de jogadoras em ordem crescente de ID
    print("\nConsulta de Jogadora por ID")
    # Exibe cada jogadora usando a função de mensagem de visualização
    for jogadora in jogadoras_ordenadas:
        mesagem_visualizacao(jogadora)

# Função para atualizar os dados de uma jogadora existente
def atualizar_jogadora():
    try:
        global jogadoras # Declara que a variável jogadoras é global para modificar seu valor
        jogadoras = ler_jogadoras() # Garante que a lista de jogadoras está atualizada
        id = mensagem_id("atualizada") # Recebe o ID da jogadora a ser atualizada
        jogadora_antiga = None # Inicializa a variável para armazenar a jogadora encontrada

        for jogadora in jogadoras: # Caso a jogadora com o ID fornecido seja encontrada, armazena na variável
            if jogadora.id == id:
                jogadora_antiga = jogadora
                break

        if not jogadora_antiga:
            raise ValueError # Se a jogadora não for encontrada, levanta um erro

        dados = mensagem_atualizacao(jogadora_antiga) # Recebe os novos dados para atualização
        jogadora_antiga.bpm, jogadora_antiga.velocidade = dados # Atualiza os dados da jogadora encontrada

        sobrescrever_arquivo(jogadoras) # Sobrescreve o arquivo com a lista atualizada de jogadoras
        
        print("\nJogadora atualizada com sucesso!")
        jogadoras = ler_jogadoras() # Recarrega a lista de jogadoras atualizada
    except (ValueError, IndexError):
        print("\nID inválido. Digite um número válido.") # Em caso de erro ou ID inválido, exibe a mensagem de erro

# Função para deletar uma jogadora existente
def deletar_jogadora():
    try:
        global jogadoras # Declara que a variável jogadoras é global para modificar seu valor
        id = mensagem_id("deletada") # Recebe o ID da jogadora a ser atualizada
        index = int(id) -1 # Converte o ID para índice (assumindo IDs sequenciais começando em 1)

        # Caso o index não seja válido, levanta um erro
        if index < 0 or index >= len(jogadoras):
            raise IndexError
        
        # Remove a jogadora da lista local
        jogadoras.pop(index)
        # Remove a jogadora do arquivo sobrescrevendo com a lista atualizada
        sobrescrever_arquivo(jogadoras)

        print("\nJogadora deletada com sucesso!")
        jogadoras = ler_jogadoras() # Recarrega a lista de jogadoras atualizada
    except (ValueError, IndexError): 
        print("\nID inválido. Digite um número válido.") # Em caso de erro ou ID inválido, exibe a mensagem de erro

# Função para consultar uma jogadora por ID
def consultar_jogadora_id():
    try:
        id = mensagem_id("consultada") # Recebe o ID da jogadora a ser consultada
        jogadora_encontrada = None # Inicializa a variável para armazenar a jogadora encontrada

        for jogadora in jogadoras: # Caso a jogadora com o ID fornecido seja encontrada, armazena na variável
            if jogadora.id == id:
                jogadora_encontrada = jogadora
                break

        mesagem_visualizacao(jogadora_encontrada) # Exibe a jogadora encontrada ou mensagem de não encontrada
    except ValueError:
        print("\nID inválido. Digite um número válido.") # Em caso de erro ou ID inválido, exibe a mensagem de erro