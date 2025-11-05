# Funções para exibir mensagens ao usuário e receber entradas

# Função para exibir o menu inicial e receber a escolha do usuário
def mensagem_incial():
    print("\nEscolha uma das seguintes opções")
    print("<1> Consultar jogadoras (ordem alfabética)\n<2> Consultar jogadoras (id)\n<3> Cadastrar Jogadoras\n<4> Atualizar Jogadora (BMP e Velocidade)")
    print("<5> Deletar Jogadoras\n<6> Consultar jogadora por id\n<7> Sair do programa")
    # Em caso de entrada inválida, retorna 0
    try:
        return int(input("Resposta: "))
    except ValueError:
        return 0
    
# Mensagem de despedida
def mensagem_final():
    print("\nAté logo!")

# Mensagem de erro para opção inválida
def mensagem_erro():
    print("\nOpção inválida! Tente novamente.")

# Função para receber os dados de cadastro de uma nova jogadora
def mensagem_cadastro():
    print("\nCadastro de Jogadoras")
    nome = input("Nome: ")
    idade = input("Idade: ")
    clube = input("Clube: ")
    bpm = input("BPM: ")
    velocidade = input("Velocidade: ")
    return nome, idade, clube, bpm, velocidade # Retorna os dados como uma tupla

# Função para exibir os dados de uma jogadora
def mesagem_visualizacao(jogadora):
    if jogadora:
        print(f"ID: {jogadora.id}, Nome: {jogadora.nome}, Idade: {jogadora.idade}, Clube: {jogadora.clube}, BPM: {jogadora.bpm}, Velocidade: {jogadora.velocidade}.")
    else:
        print("Nenhuma jogadora encontrada.") # Mensagem caso a jogadora não seja encontrada

# Função para receber os novos dados para atualização de uma jogadora
def mensagem_atualizacao(jogadora):
    print(f"\nAtualização de {jogadora.nome}")
    bpm = input("Novo BPM: ")
    velocidade = input("Nova Velocidade: ")
    return bpm, velocidade # Retorna os novos dados como uma tupla

# Função para receber o ID da jogadora para ações como atualização, deleção ou consulta
def mensagem_id(acao):
    try:
        return input(f"\nDigite o ID da jogadora a ser {acao}: ")
    except ValueError:
        return "Digite um número válido." # Retorna mensagem de erro em caso de entrada inválida

# Mensagem para pausar o programa e esperar o usuário pressionar Enter
def continuar():
    return "\nPressione Enter para continuar..." 