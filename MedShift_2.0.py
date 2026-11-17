class Medico:
    def __init__(self, id_med, nome, espec, disp_m, disp_t, disp_n):
        self.id = id_med
        self.nome = nome
        self.espec = espec
        self.disp_m = disp_m
        self.disp_t = disp_t
        self.disp_n = disp_n
        self.qtd_t = [0] * 7
def menu():
    medicos = [None] * 140
    semana = []
    for i in range(7):
        semana.append([[],[],[]])
    while True: 
        print("=== Menu Principal ===")
        print("=== Escolha uma opção ===")
        try:
            opcao = int(input("(1) => Cadastro\n(2) => Consulta\n(3) => Construção de Escalas\n(4) => Menu de Validações\n(5) => Encerrar Programa\n"))
        except ValueError:
            print("Valor Inválido")
            continue
        if opcao == 1:
            cadastro(medicos)
        elif opcao == 2:
            consulta(medicos)
        elif opcao == 3:
            construção(medicos,semana)
        elif opcao == 4:
            validacao(medicos,semana)
        elif opcao == 5:
            print("\nEncerrando Programa\n")
            break
        else: 
            print("\nOpção Inválida\n")
def cadastro(lista):
    while True:
        print("\n=== Menu de Cadastros ===")
        opcao = input("(1) => Cadastrar médicos\n(2) => Excluir cadastros\n(3) => Sair\n")
        continuar = True
        if opcao == "1": 
            print("\n=== Cadastramento ===")
            while continuar:
                for i in range(len(lista)):
                    if lista[i] is None:
                        nome_med = input("\nDigite o nome do médico:\n")
                        print("\nQual a especialidade do médico?")
                        while True:
                            try:
                                espec_med = int(input("(1) => Clínico Geral\n(2) => Pediatra\n(3) => Cirurgião\n"))
                            except ValueError:
                                print("Valor Inválido")
                                continue
                            if espec_med in (1, 2, 3):
                                break
                            else:
                                print("\nValor inválido\n")
                                continue
                        print("\nEle tem disponibilidade para escalas no período da MANHÃ?")
                        while True:
                            disp_m = input("(1) => Sim\n(2) => Não\n")
                            if disp_m in ("1", "2"):
                                break
                            else:
                                print("\nValor inválido\n")
                                continue
                        print("\nEle tem disponibilidade para escalas no período da TARDE?")
                        while True:
                            disp_t = input("(1) => Sim\n(2) => Não\n")
                            if disp_t in ("1", "2"):
                                break
                            else:
                                print("\nValor inválido\n")
                                continue
                        print("\nEle tem disponibilidade para escalas no período da NOITE?")
                        while True:
                            disp_n = input("(1) => Sim\n(2) => Não\n")
                            if disp_n in ("1", "2"):
                                break
                            else:
                                print("\nValor inválido\n")
                                continue
                        ident = i + 1
                        medico = Medico(ident, nome_med, espec_med, disp_m, disp_t, disp_n)
                        lista[i] = medico
                        break
                else:
                    print("\nNão há espaços livres para novos cadastros\n")
                    break
                print("\nDeseja cadastrar outro Médico?")
                while True:
                    opcao = input("Digite '1' para SIM e '2' para NÃO:\n")
                    if opcao == "1":
                        break
                    elif opcao == "2":
                        continuar = False
                        break
                    else:
                        print("\nOpção inválida, digite apenas '1' para SIM ou '2' para NÃO!\n")
                        continue
        elif opcao == "2":
            print("\n=== Exclusão de cadastros ===\n")
            while continuar: 
                try:
                    opcao = int(input("\nDigite o ID do cadastro que você quer excluir:\n"))
                    i = opcao - 1
                except ValueError:
                    print("\nValor inválido!\n")
                    continue
                if i in range(len(lista)):
                    if lista[i] is None:
                        print("\nNão existe um cadastro nesta posição")
                    elif lista [i] is not None:
                        lista[i] = None
                        print("\nCadastro excluído com sucesso")
                else:
                    print("\nValor inválido\n")
                print("\nDeseja excluir outro cadastro?")
                while True:
                    opcao = input("Digite '1' para SIM e '2' para NÃO:\n").capitalize()
                    if opcao == "1":
                        break
                    elif opcao == "2":
                        continuar = False
                        break
                    else:
                        print("\nOpção inválida, digite apenas '1' para SIM ou '2' para NÃO\n")
                        continue
        elif opcao == "3":
            print("\n=== Retornando ao menu principal ===\n")
            break
        else:
            print("\nOpção inválida!\n")
    return lista
def consulta(lista):
    especialidades = {1:"Clínico Geral", 2:"Pediatra", 3:"Cirurgião"}
    disponibilidade = {"1":"Sim", "2":"Não"}
    while True:
        try:
            opcao = int(input("Digite o ID que você quer consultar:\n"))
            break
        except ValueError:
            print("\nValor Inválido\n")
            continue
    i = opcao - 1
    if i in range(len(lista)):
        if lista[i] is None:
            print("\nNão há cadastros nesta posição\n")
        else:
            print(f"\nID => {lista[i].id}")
            print(f"Nome => {lista[i].nome}")
            print(f"Especialidade => {especialidades[lista[i].espec]}")
            print(f"Disponível de MANHÃ? => {disponibilidade[lista[i].disp_m]}")
            print(f"Disponível de TARDE? => {disponibilidade[lista[i].disp_t]}")
            print(f"Disponível de NOITE? => {disponibilidade[lista[i].disp_n]}")
            print(f"Quantidade de TURNOS na semana => {sum(lista[i].qtd_t)} turno(s)\n")
    else:
        print("\nValor Inválido\n")
def construção(lista, matriz):
    print("=== Menu de Construção de Escalas ===")
    while True:
        try:
            opcao = int(input("(1) => Construir Escalas\n(2) => Sair\n"))
        except ValueError:
            print("\nValor inválido\n")
            continue
        if opcao == 1:
            if any(medico is not None in lista for medico in lista):
                while True:
                    print("Escolha um dia da semana:")
                    try:
                        opcao_d = int(input("(1) => Domingo\n(2) => Segunda\n(3) => Terça\n(4) => Quarta\n(5) => Quinta\n(6) => Sexta\n(7) => Sábado\n"))
                    except ValueError:
                        print("\nOpção inválida\n")
                        continue
                    print("\nEscolha um turno:")
                    try:
                        opcao_t = int(input("(1) => Manhã\n(2) => Tarde\n(3) => Noite\n"))
                    except ValueError:
                        print("\nOpção inválida\n")
                        continue
                    x = opcao_d - 1
                    y = opcao_t - 1
                    atualizacao(x,y,lista,matriz,operacao=-1)
                    cadastro_escala(x,y,lista,matriz)
                    break
            else:
                print("\nNão há cadastros no sistema. Cadastre pelo menos um médico para prosseguir!\n")
        elif opcao == 2:
            print("\n=== Retornando ao menu principal ===\n")
            break
        else: 
            print("\nOpção inválida\n")
            continue
def cadastro_escala(x,y,lista,matriz):
    e = 0
    dias = {0:"Domingo", 1:"Segunda", 2:"Terça", 3:"Quarta", 4:"Quinta", 5:"Sexta", 6:"Sábado"}
    turnos = {0:"Manhã", 1:"Tarde", 2:"Noite"}
    espec_dict = {0:"Clínico Geral", 1:"Pediatra", 2:"Cirurgião"}
    erros_dict = {1:"Erro! Limite diário de escalas excedido.\n", 2:"Erro! O profissional já está escalado no turno noturno anterior\n",
             3:"Erro! O profissional já está escalado no turno matutino posterior.\n", 4:"Erro! Limite semanal de escalas excedido\n", 
             5:"Erro! O profissional já está escalado neste turno\n", 6:"Erro! Especialidade errada\n",
             7:"Erro! Não há cadastro relacionado a este ID\n"}
    atributos = {0:"disp_m", 1:"disp_t", 2:"disp_n" }
    print(f"\n=== Você está no turno de {dias[x]} no período da {turnos[y]} ===\n")
    continuar = True
    while continuar:
        if any(medico.espec == 1 and getattr(medico, atributos[y]) == "1" for medico in lista if medico is not None):
            print("Você tem a disposição os seguintes CLÍNICOS GERAIS:\n")
            cont = 0
            for i in range(len(lista)):  
                if lista[i] is None:
                    continue
                elif getattr(lista[i], atributos[y]) == "1" and lista[i].espec == 1:
                    ident = i + 1
                    cont = cont + 1
                    print(f"Profissional nº{cont}:\nID => {ident}\nNome => {lista[i].nome}\n")
            while True:
                try:
                    id_med = int(input("Digite um ID\n"))
                except ValueError:
                    print("\nValor inválido!\n")
                    continue
                if id_med > 0 and id_med < 141:
                    erros = checagens(lista,matriz,x,y,id_med,e)
                    if not erros:
                        matriz[x][y].append(id_med)
                        lista[id_med-1].qtd_t[x] += 1
                        break
                    else:
                        for i in erros:
                            print(erros_dict[i])
                        break
                else: 
                    print("\nValor Inválido\n")
            print("Deseja cadastrar outro CLÍNICO GERAL?\n")
            while True:
                opcao = input("Digite '1' para SIM e '2' para NÃO:\n")
                if opcao == "1":
                    break
                elif opcao == "2":
                    continuar = False
                    break
                else:
                    print("\nOpção inválida, digite apenas '1' para SIM ou '2' para NÃO!\n")
                    continue
        else:
            print(f"\nVocê não possui Clínicos Gerais disponíveis no período da {turnos[y]}\n")
            break
    continuar = True
    while continuar:
        if any(medico.espec == 2 and getattr(medico, atributos[y]) == "1" for medico in lista if medico is not None):
            print("Você tem a disposição os seguintes PEDIATRAS:\n")
            cont = 0
            for i in range(len(lista)):  
                if lista[i] is None:
                    continue
                elif getattr(lista[i], atributos[y]) == "1" and lista[i].espec == 2:
                    ident = i + 1
                    cont += 1
                    print(f"Profissional nº{cont}:\nID => {ident}\nNome => {lista[i].nome}\n")
            while True:
                try:
                    id_med = int(input("Digite um ID\n"))
                except ValueError:
                    print("\nValor inválido!\n")
                    continue
                if id_med > 0 and id_med < 141:
                    e = 1
                    erros = checagens(lista,matriz,x,y,id_med,e)
                    if not erros:
                        matriz[x][y].append(id_med)
                        lista[id_med-1].qtd_t[x] += 1
                        break
                    else:
                        for i in erros:
                            print(erros_dict[i])
                        break
                else: 
                    print("\nValor Inválido\n")
            print("\nDeseja cadastrar outro PEDIATRA?\n")
            while True:
                opcao = input("Digite '1' para SIM e '2' para NÃO:\n")
                if opcao == "1":
                    break
                elif opcao == "2":
                    continuar = False
                    break
                else:
                    print("\nOpção inválida, digite apenas '1' para SIM ou '2' para NÃO!\n")
                    continue
        else:
            print(f"\nVocê não possui Pediatras disponíveis no período da {turnos[y]}\n")
            break
    continuar = True
    while continuar:
        if any(medico.espec == 3 and getattr(medico, atributos[y]) == "1" for medico in lista if medico is not None):
            print("Você tem a disposição os seguintes CIRURGIÕES:\n")
            cont = 0
            for i in range(len(lista)):  
                if lista[i] is None:
                    continue
                elif getattr(lista[i], atributos[y]) == "1" and lista[i].espec == 3:
                    ident = i + 1
                    cont = cont + 1
                    print(f"Profissional nº{cont}:\nID => {ident}\nNome => {lista[i].nome}\n")
            while True:
                try:
                    id_med = int(input("Digite um ID\n"))
                except ValueError:
                    print("\nValor inválido!\n")
                    continue
                if id_med > 0 and id_med < 141:
                    e = 2
                    erros = checagens(lista,matriz,x,y,id_med,e)
                    if not erros:
                        matriz[x][y].append(id_med)
                        lista[id_med-1].qtd_t[x] += 1
                        break
                    else:
                        for i in erros:
                            print(erros_dict[i])
                        break
                else: 
                    print("\nValor Inválido\n")
            print("Deseja cadastrar outro CIRURGIÃO?")
            while True:
                opcao = input("Digite '1' para SIM e '2' para NÃO:\n")
                if opcao == "1":
                    break
                elif opcao == "2":
                    continuar = False
                    break
                else:
                    print("\nOpção inválida, digite apenas '1' para SIM ou '2' para NÃO!\n")
                    continue
        else:
            print(f"Você não possui Cirurgiões disponíveis no período da {turnos[y]}\n")
            break
    print("\nEscala Salva! Retornando ao menu de Construção de Escalas\n")
    return matriz
def checagens(lista,matriz,x,y,id_med,e):
    erros = [] 
    prox_dia = (x+1)%7
    dia_ant = (6+x)%7
    if lista[id_med-1] is None:
        erros.append(7)
    else:
        total_semana = sum(lista[id_med-1].qtd_t)
        #1 No máximo 2 turnos no mesmo dia
        if lista[id_med-1].qtd_t[x] >= 2:
            erros.append(1)        
        #2 Turno noturno não pode ser seguido de matutino e vice-versa
        if y == 0: 
            if id_med in matriz[dia_ant][2] and id_med in matriz[x][0]:
                erros.append(2)
        elif y == 2:
            if id_med in matriz[x][2] and id_med in matriz[prox_dia][0]:
                erros.append(3)
        #3 Máximo de 8 turnos na semana
        if total_semana >= 8:
            erros.append(4)
        #4 Médico já cadastrado no turno
        if id_med in matriz[x][y]:
            erros.append(5)
        #5 Especialidade diferente da solicitada
        if lista[id_med-1].espec != (e+1):
            erros.append(6)
    return erros
def atualizacao(x,y,lista,matriz,operacao):
    for id in matriz[x][y]:
        lista[id-1].qtd_t[x] += operacao
def validacao(lista,matriz):
    while True: 
        print("=== Menu de Validações ===")
        print("=== Escolha uma opção ===")
        try:
            opcao = int(input("(1) => Validação Diária\n(2) => Validação Semanal\n(3) => Sair\n"))
        except ValueError:
            print("\nValor Inválido\n")
            continue
        if opcao == 1:
            validacao_diaria(lista,matriz)
        elif opcao == 2:
            validacao_semanal(lista,matriz)
        elif opcao == 3:
            print("\n=== Retornando ao Menu Principal===\n")
            break
        else: 
            print("\nOpção Inválida\n") 
def validacao_diaria(lista,matriz):
    dias = {0:"Domingo", 1:"Segunda", 2:"Terça", 3:"Quarta", 4:"Quinta", 5:"Sexta", 6:"Sábado"}
    turnos = {0:"Manhã", 1:"Tarde", 2:"Noite"}
    erros_dict = {0:"\nTurno Aprovado\n", 1:"Erro! Faltam Clinicos Gerais", 2:"Erro! Faltam Pediatras", 3:"Erro! Faltam Cirurgiões", 4:"Plantão 24 Hrs Aprovado!"}
    espec_dict = {0:"Clínicos Gerais", 1:"Pediatras", 2:"Cirurgiões"}
    erros =[]
    while True: 
        print("=== Validações de Escalas ===")
        print("=== Escolha um dia ===")
        try:
            x = int(input("(1) => Domingo\n(2) => Segunda\n(3) => Terça\n(4) => Quarta\n(5) => Quinta\n(6) => Sexta\n(7) => Sábado\n"))
        except ValueError:
            print("\nValor Inválido\n")
            continue
        print("\n=== Qual turno você deseja validar? ===")
        try:
            y = int(input("(1) => Manhã\n(2) => Tarde\n(3) => Noite\n(4) => Plantão 24 Hrs (3 Turnos Juntos)\n"))
        except ValueError:
            print("\nValor Inválido\n")
            continue
        x -= 1
        y -= 1
        if y == 3:
            #Validação do Plantão 24 Hrs
            turno_M = contagem_espec(x,0,lista,matriz)
            turno_T = contagem_espec(x,1,lista,matriz)
            turno_N = contagem_espec(x,2,lista,matriz)
            turnos_dia = [turno_M,turno_T,turno_N]
            cl =[]
            p =[]
            c=[]
            for i in range(len(turnos_dia)):
                print(f"\nPlantão da {turnos[i]}\n")
                if all(j == 0 for j in turnos_dia[i]):
                    print("O turno não possui profissionais cadastrados\n")
                else:
                    for espec in range(len(turnos_dia[i])):
                        print(f"Você possui {turnos_dia[i][espec]} {espec_dict[espec]} cadastrados")
            for turno in turnos_dia:
                cl.append(max(0, 2-turno[0]))
                p.append(max(0, 1-turno[1]))
                c.append(max(0, 1-turno[2]))
            if any(cl) or any(p) or any(c): 
                for n in range(3):
                    if cl[n] > 0:
                        print(f"\nErro! Faltam {cl[n]} Clínicos Gerais no turno da {turnos[n]}")
                    if p[n] > 0:
                        print(f"\nErro! Faltam {p[n]} Pediatras no turno da {turnos[n]}")
                    if c[n] > 0:
                        print(f"\nErro! Faltam {c[n]} Cirurgiões no turno da {turnos[n]}")
            else:
                print(erros_dict[4])          
            break
        elif y in turnos:
            #Validação do turno específico e impressão de relatórios
            print(f"\nVocê selecionou o turno de {dias[x]} de {turnos[y]}\n")
            espec_quant = contagem_espec(x,y,lista,matriz)
            if espec_quant[0] < 2:
                erros.append(1)
            if espec_quant[1] < 1:
                erros.append(2)
            if espec_quant[2] < 1:
                erros.append(3)
            if not erros:
                erros.append(0)
            print(f"Você possui {espec_quant[0]} Clínicos Gerais cadastrados")
            print(f"Você possui {espec_quant[1]} Pediatras cadastrados")
            print(f"Você possui {espec_quant[2]} Cirurgiões cadastrados")
            for i in erros:
                print(erros_dict[i])
            print("\n=== Lista de Profissionais Escalados ===\n")
            for i in range(len(espec_quant)):
                if espec_quant[i] == 0:
                    print(f"Não há {espec_dict[i]} cadastrados neste turno\n")
                else:
                    print(espec_dict[i])
                    for id in matriz[x][y]:    
                        if lista[id-1].espec == i+1:                     
                            print(f"ID => {lista[id-1].id}")
                            print(f"Nome => {lista[id-1].nome}")
                            print(f"Especialidade => {espec_dict[i]}\n")
            break
        else: 
            print("\nOpção Inválida\n") 
def contagem_espec(x,y,lista,matriz):
    espec = []
    for id in matriz[x][y]:
        espec.append(lista[id-1].espec)
    cl = espec.count(1)
    p = espec.count(2)
    c = espec.count(3)
    espec_quant = [cl,p,c]
    return espec_quant
def validacao_semanal(lista,matriz):
    while True: 
        print("=== Validações Semanais ===")
        print("=== Escolha uma opção ===")
        try:
            opcao = int(input("(1) => Média de Escalas\n(2) => Porcentagem de Turnos Cobertos\n(3) => Validação da Semana\n(4) => Sair\n"))
        except ValueError:
            print("\nValor Inválido\n")
            continue
        if opcao == 1:
            media_escalas(lista)
        elif opcao == 2:
            cobertura_turnos(lista,matriz)
        elif opcao == 3:
            validacao_semana(lista,matriz)
        elif opcao == 4:
            break
        else: 
            print("\nOpção Inválida\n") 
def media_escalas(lista):
    espec_dict = {0:"Clínico Geral", 1:"Pediatra", 2:"Cirurgião"}
    total_atribuicoes = []
    mais_turnos = []
    menos_turnos = []
    for i in range(len(lista)):
        if lista[i] is not None:
            total_atribuicoes.append([lista[i].id, sum(lista[i].qtd_t)])
    if len(total_atribuicoes) > 0:
        maior = max(i[1] for i in total_atribuicoes)
        menor = min(i[1] for i in total_atribuicoes)
    else: 
        maior = 0
        menor = 0
    for i in range(len(total_atribuicoes)):
        if total_atribuicoes[i][1] == maior:
            mais_turnos.append(total_atribuicoes[i][0])
        if total_atribuicoes[i][1] == menor:
            menos_turnos.append(total_atribuicoes[i][0])
    total_cadastros = len(total_atribuicoes)
    total_turnos = sum(i[1] for i in total_atribuicoes)
    if total_cadastros != 0:
        media_equipe = total_turnos/total_cadastros
    else:
        media_equipe = 0
    print("\n=== Média de Escalas ===\n")
    print(f"Maior carga de atribuição: {maior} turno(s)")
    print(f"Menor carga de atribuição: {menor} turno(s)")
    print(f"Valor médio de atribuições: {media_equipe:.2f} escalas por profissional")
    print("\nProfissionais com o MAIOR número de escalas atribuídas")
    if not mais_turnos:
        print("Não há nenhuma atribuição de escala na semana")
    else:
        for i in range(len(mais_turnos)):
            print(f"ID => {lista[mais_turnos[i]-1].id}")
            print(f"Nome => {lista[mais_turnos[i]-1].nome}")
            print(f"Especialidade => {espec_dict[lista[mais_turnos[i]-1].espec-1]}\n")
            print(f"Total de Atribuições => {sum(lista[mais_turnos[i]-1].qtd_t)}")
    print("\nProfissionais com o MENOR número de escalas atribuídas")
    if not mais_turnos:
            print("Não há nenhuma atribuição de escala na semana\n")
    else:
        for i in range(len(menos_turnos)):
            print(f"ID => {lista[menos_turnos[i]-1].id}")
            print(f"Nome => {lista[menos_turnos[i]-1].nome}")
            print(f"Especialidade => {espec_dict[lista[menos_turnos[i]-1].espec-1]}\n")
            print(f"Total de Atribuições => {sum(lista[menos_turnos[i]-1].qtd_t)}\n")
    if any(sum(medico.qtd_t) > media_equipe for medico in lista if medico is not None):
        print("\nProfissionais que ultrapassaram a média de atribuições da equipe:\n")
        for i in range(len(total_atribuicoes)):
            if total_atribuicoes[i][1] > media_equipe:
                print(f"\nID => {lista[total_atribuicoes[i][0]-1].id}")
                print(f"Nome => {lista[total_atribuicoes[i][0]-1].nome}")
                print(f"Especialidade => {espec_dict[lista[total_atribuicoes[i][0]-1].espec-1]}\n")
                print(f"Total de Atribuições => {sum(lista[total_atribuicoes[i][0]-1].qtd_t)}\n")
def cobertura_turnos(lista,matriz):
    turnos_cobertos = turnos_validos(lista,matriz)
    turnos_incompletos = 21 - turnos_cobertos
    porcentagem = (turnos_cobertos/21)*100
    print("=== Cobertura de Turnos ===\n")
    print(f"{porcentagem:.2f}% da semana com cobertura adequada")
    print(f"Você tem {turnos_cobertos} turno(s) devidamente coberto(s)")
    print(f"Você tem {turnos_incompletos} turno(s) sem a cobertura adequada\n")
def turnos_validos(lista,matriz):
    turnos_cobertos = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            turno_dia = contagem_espec(x,y,lista,matriz)
            if turno_dia[0] >= 2 and turno_dia[1] >= 1 and turno_dia[2] >= 1:
                turnos_cobertos += 1
    return turnos_cobertos
def validacao_semana(lista,matriz):
    dias = {0:"Domingo", 1:"Segunda", 2:"Terça", 3:"Quarta", 4:"Quinta", 5:"Sexta", 6:"Sábado"}
    turnos = {0:"Manhã", 1:"Tarde", 2:"Noite"}
    espec_dict = {0:"Clínicos Gerais", 1:"Pediatras", 2:"Cirurgiões"}
    pendencias = []
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            turno_dia = contagem_espec(x,y,lista,matriz)
            if turno_dia[0] < 2:
                pendencias.append([x,y,0])
            if turno_dia[1] < 1:
                pendencias.append([x,y,1])
            if turno_dia[2] < 1:
                pendencias.append([x,y,2])
    print("=== Validação da Semana ===\n")
    if not pendencias:
        print("Semana validada com Sucesso! Todos os turnos estão devidamente cobertos!\n")
    else:
        print("Semana inválida!\n")
        for i in pendencias:
            print(f"Erro! Faltam {espec_dict[i[2]]} no turno da {turnos[i[1]]} de {dias[i[0]]}") 
    print()       
menu()