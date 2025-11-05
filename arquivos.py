from jogadora import Jogadora # Importa a classe Jogadora para manipulação dos objetos jogadora

# Método para ler o arquivo CSV e retornar uma lista de objetos Jogadora
def ler_jogadoras():
    try:
        linhas = []
        jogadoras = []
        with open("jogadoras.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas[1:]:
            jogadoras.append(Jogadora(*linha.strip().split(";")))
    except FileNotFoundError:
        criar_arquivo()
        jogadoras = []
    return jogadoras

# Método para escrever uma nova jogadora no arquivo CSV
def escrever(jogadora):
    with open("jogadoras.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{jogadora.id};{jogadora.nome};{jogadora.idade};{jogadora.clube};{jogadora.bpm};{jogadora.velocidade}\n")

# Método para criar o arquivo CSV caso ele não exista
def criar_arquivo():
    with open("jogadoras.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write("id;nome;idade;clube;bpm;velocidade\n")

# Método para sobrescrever o arquivo CSV com uma nova lista de jogadoras, proporcionada pelo método atualizar e deletar
def sobrescrever_arquivo(jogadoras):
    with open("jogadoras.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write("id;nome;idade;clube;bpm;velocidade\n")
        for jogadora in jogadoras:
            # Método para escrever cada jogadora no arquivo
            arquivo.write(f"{jogadora.id};{jogadora.nome};{jogadora.idade};{jogadora.clube};{jogadora.bpm};{jogadora.velocidade}\n")