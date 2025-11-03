def ler_jogadoras():
    linhas = []
    with open("jogadoras.csv", "r") as arquivo:
        linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())

def escrever(jogadora):
    with open("jogadoras.csv", "a") as arquivo:
        arquivo.write(f"{jogadora.nome},{jogadora.idade},{jogadora.clube},{jogadora.bpm},{jogadora.velocidade}\n")