def mensagem_incial():
    print("\nEscolha uma das seguintes opções")
    print("<1> Consultar jogadoras (ordem alfabética)\n<2> Cadastrar Jogadoras\n<3>Atualizar Jogadora")
    print("<4> Deletar Jogadoras\n<5> Consultar jogadora por id\n<6> Sair do programa")
    try:
        return int(input("Resposta: "))
    except ValueError:
        return 0