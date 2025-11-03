def mensagem_incial():
    print("\nEscolha uma das seguintes opções")
    print("<1> Consultar jogadoras (ordem alfabética)\n<2> Cadastrar Jogadoras\n<3> Atualizar Jogadora (BMP e Velocidade)")
    print("<4> Deletar Jogadoras\n<5> Consultar jogadora por id\n<6> Sair do programa")
    try:
        return int(input("Resposta: "))
    except ValueError:
        return 0
    
def mensagem_final():
    print("\nAté logo!")
    
def mensagem_erro():
    print("\nOpção inválida! Tente novamente.")

def mensagem_cadastro():
    print("\nCadastro de Jogadoras")
    nome = input("Nome: ")
    idade = input("Idade: ")
    clube = input("Clube: ")
    bpm = input("BPM: ")
    velocidade = input("Velocidade: ")
    return nome, idade, clube, bpm, velocidade

def mesagem_visualizacao(jogadora):
    if jogadora:
        print(f"ID: {jogadora.id}, Nome: {jogadora.nome}, Idade: {jogadora.idade}, Clube: {jogadora.clube}, BPM: {jogadora.bpm}, Velocidade: {jogadora.velocidade}.")
    else:
        print("Nenhuma jogadora encontrada.")

def mensagem_atualizacao():
    print("\nAtualização de Jogadora")
    bpm = input("Novo BPM: ")
    velocidade = input("Nova Velocidade: ")
    return bpm, velocidade

def mensagem_id(acao):
    try:
        return int(input(f"\nDigite o ID da jogadora a ser {acao}: "))
    except ValueError:
        return "Digite um número válido."