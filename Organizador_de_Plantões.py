def menu():
    while True: 
        print("\n===Sistema de Plantões Médicos===\n")
        print("Selecione uma opção:")
        try:
            opcao = int(input("1-Contabilizar médicos disponíveis\n2-Sair\n"))
        except ValueError:
            print("\nValor inválido! Digite apenas '1' ou '2'!")
            continue
        if opcao == 1:
            med_total = contagem_med()
            turnos_validados = validacao_turnos(med_total)
            relatorio_1(med_total)
            checagem(turnos_validados,med_total)
        elif opcao == 2:
            print("\nPrograma Finalizado!")
            break
        else:
            print("Opção inválida")
def confirmar():
    while True:
        print("\nVocê confirma a entrada desses dados? (Digite S para 'SIM' e N para 'NÃO')")
        try:
            resposta = str(input())
        except ValueError:
            print("Valor Inválido! Digite apenas 'S' ou 'N'!")
            continue
        if resposta.upper() == "N":
            print("\nInsira novamente os valores")
            return False                       
        elif resposta.upper() == "S": 
            return True
        else:
            print("\nResposta inválida, confirme novamente")
def contagem_med():
    while True:
        try:
            med_max = int(input("\nQual a capacidade máxima de médicos o seu hospital suporta? "))
        except ValueError:
            print("\nValor inválido! Digite um número inteiro!")
            continue
        print(f"\nSeu hospital comporta {med_max} médicos.")
        if confirmar():
            break
        else:
            continue
    while True:
        print("\nPara a escala da MANHÃ: ")
        try:
            cgM = int(input("Quantos Clínicos Gerais você tem a disposição? "))
            pM = int(input("Quantos Pediatras você tem a disposição? "))
            cM = int(input("Quantos Cirurgiões você tem a disposição? "))
        except ValueError:
            print("\nValor inválido! Digite um número inteiro!")
            continue
        if cgM < 0 or pM < 0 or cM < 0:
            print("\nValores inválidos, você inseriu valores negativos! \nPor favor insira novamente a quantidade de médicos disponíveis para MANHÃ\n")
            continue
        elif cgM+pM+cM > med_max:
            print("\nValores inválidos, você tem médicos demais! \nPor favor insira novamente a quantidade de médicos disponíveis para MANHÃ\n")
            continue
        else:
            print("\nOs valores inseridos foram:")
            print(f"{cgM} Clínico(s) Geral(is)\n{pM} Pediatra(s)\n{cM} Cirurgiõe(s)") 
            if confirmar():
                break
            else:
                continue                 
    while True:
        print("\nPara a escala da TARDE: ")
        try:
            cgT = int(input("Quantos Clínicos Gerais você tem a disposição? "))
            pT = int(input("Quantos Pediatras você tem a disposição? "))
            cT = int(input("Quantos Cirurgiões você tem a disposição? "))
        except ValueError:
            print("\nValor inválido! Digite um número inteiro!")
            continue
        if cgT < 0 or pT < 0 or cT < 0:
            print("\nValores inválidos, você inseriu valores negativos! \nPor favor insira novamente a quantidade de médicos disponíveis para TARDE\n")
            continue
        elif cgT+pT+cT > med_max:
            print("\nValores inválidos, você tem médicos demais! \nPor favor insira novamente a quantidade de médicos disponíveis para NOITE\n")
            continue
        else:
            print("\nOs valores inseridos foram:")
            print(f"{cgT} Clínico(s) Geral(is)\n{pT} Pediatra(s)\n{cT} Cirurgiõe(s)")
            if confirmar():
                break
            else:
                continue
    while True:
        print("\nPara a escala da NOITE: ")
        try:
            cgN = int(input("Quantos Clínicos Gerais você tem a disposição? "))
            pN = int(input("Quantos Pediatras você tem a disposição? "))
            cN = int(input("Quantos Cirurgiões você tem a disposição? "))
        except ValueError:
            print("\nValor inválido! Digite um número inteiro!")
            continue
        if cgN < 0 or pN < 0 or cN < 0:
            print("\nValores inválidos, você inseriu valores negativos! \nPor favor insira novamente a quantidade de médicos disponíveis para NOITE\n")
            continue
        elif cgN+pN+cN > med_max:
            print("Valores inválidos, por favor insira novamente a quantidade de médicos disponíveis para NOITE")
            continue
        else:
            print("\nOs valores inseridos foram:")
            print(f"{cgN} Clínicos Gerais\n{pN} Pediatras\n{cN} Cirurgiões")
            if confirmar():
                break
            else:
                continue
    manha = [cgM, pM, cM]
    tarde = [cgT, pT, cT]
    noite = [cgN, pN, cN]
    med_total = [manha, tarde, noite]
    return med_total
def validacao_turnos(matriz):
    for i in range(3):
        if matriz[0][i]<2: 
            return False
        elif matriz[1][i]<1:
            return False
        elif matriz[2][i]<1:
            return False
        else: 
            return True
def relatorio_1 (matrizA):
    print("\nRelatório geral:")
    print(f"Para o turno da MANHÃ, você tem a disposição:")
    print(f"{matrizA[0][0]} Clinico(s) Geral(is)\n{matrizA[0][1]} Pediatra(s)\n{matrizA[0][2]} Cirugião(ões)")
    print(f"\nPara o turno da TARDE, você tem a disposição:")
    print(f"{matrizA[1][0]} Clinico(s) Geral(is)\n{matrizA[1][1]} Pediatra(s)\n{matrizA[1][2]} Cirugião(ões)")
    print(f"\nPara o turno da NOITE, você tem a disposição:")
    print(f"{matrizA[2][0]} Clinico(s) Geral(is)\n{matrizA[2][1]} Pediatra(s)\n{matrizA[2][2]} Cirugião(ões)")
def checagem(matrizA,matrizB):
        if matrizA == True:
            print("\nRelatório final: \nO plantão é VÁLIDO e está pronto para ser publicado\n")
        else:
            turnos = ["MANHÃ","TARDE","NOITE"]
            print("\nRelatório final: \nO plantão é INVÁLIDO e não pode ser publicado")
            for i in range(3):
                if matrizB[i][0]<2:
                    print(f"Motivo: Faltam CLÍNICOS GERAIS de {turnos[i]}!")
            for i in range(3):        
                if matrizB[i][1]<1:
                    print(f"Motivo: Faltam PEDIATRAS de {turnos[i]}!")
            for i in range(3):
                if matrizB[i][2]<1:
                    print(f"Motivo: Faltam CIRURGIÕES de {turnos[i]}!")
menu()
print("\nTestando 'merge' da 'main' para 'dev'\n")