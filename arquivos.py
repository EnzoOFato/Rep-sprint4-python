from jogadora import Jogadora

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

def escrever(jogadora):
    with open("jogadoras.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{jogadora.id};{jogadora.nome};{jogadora.idade};{jogadora.clube};{jogadora.bpm};{jogadora.velocidade}\n")

def criar_arquivo():
    with open("jogadoras.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write("id;nome;idade;clube;bpm;velocidade\n")

def sobrescrever_arquivo(jogadoras):
    with open("jogadoras.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write("id;nome;idade;clube;bpm;velocidade\n")
        for jogadora in jogadoras:
            arquivo.write(f"{jogadora.id};{jogadora.nome};{jogadora.idade};{jogadora.clube};{jogadora.bpm};{jogadora.velocidade}\n")