while continuar:
    for i in range(len(medicos)):
        if medicos[i] is None:
            #efetua cadastro
            #registra o cadastro
            break
    else:
        print("Não há espaços livres para novos cadastros")
        break
    print("Deseja cadastrar outro Médico?")
    while True:
        opcao = input("Digite 'S' para SIM e 'N' para NÃO:").capitalize()
        if opcao == "S":
            break
        elif opcao == "N":
            continuar = False
            break
        else:
            print("Opção inválida, digite apenas 'S' para SIM ou 'N' para NÃO!")
            continue